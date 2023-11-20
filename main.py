import json
import logging
import subprocess
import os
import signal
import time
import ruamel.yaml
import shutil
from slugify import slugify
from chal_types.utils import WorkDir, fwrite, get_cache_state, get_challenge_hash, set_used_ports
from os.path import join


from chal_types import challenge_types, load_chal_from_config, chal_to_kube_config, gen_kube, mkdir_p, logger
from chal_types import GeneratedChallenge, ChallengeHost, ChallengeEnvironment
from chal_types.web import TemplateInjection

import rich_click as click
from rich import print
from rich.status import Status
from rich.panel import Panel


@click.group()
@click.pass_context
def chalgen(cmd):
    pass


@click.group(help="Generate or run competitions")
@click.pass_context
def comp(cmd):
    pass


@click.group(help="Generate or run challenges")
@click.pass_context
def chal(cmd):
    pass


def generate_kube_deploy(kube_dir, trees, local, reg_url, base_url):
    configs = []
    for tree in trees:
        def traverse(tree):
            if 'children' not in tree:
                return []

            kube_configs = []
            for child in tree['children']:
                kube_configs.extend(traverse(child))
                chal = child['chal']
                if chal.container_id:
                    kube_config = chal_to_kube_config(
                        chal, reg_url, local, chal.display_port, isinstance(chal, TemplateInjection), base_url)
                    kube_configs.append(kube_config)

            return kube_configs

        chal = tree['chal']
        if chal.container_id:
            kube_config = chal_to_kube_config(
                chal, reg_url, local, chal.display_port, isinstance(chal, TemplateInjection), base_url)
            configs.append(kube_config)

        chal = tree.get('host')
        if chal and chal.container_id:
            kube_config = chal_to_kube_config(
                chal, reg_url, local, 8200, isinstance(chal, TemplateInjection), base_url)
            configs.append(kube_config)

        configs.extend(traverse(tree))

    gen_kube(kube_dir, configs, local, base_url)

    return configs


def generate_challenge_graph(trees, competition_folder):
    def traverse(tree):
        if 'children' not in tree or tree['children'] == []:
            return []

        edges = []
        for child in tree['children']:
            edges.append(f'\t"{tree["name"]}"->"{child["name"]}";')
            edges.extend(traverse(child))
        return edges

    edges = []
    for tree in trees:
        if (tree['children'] == []):
            edges.append(f'\t"{tree["name"]}";')
        else:
            edges.extend(traverse(tree))

    formatted_edges = "\n".join(edges)
    graph = f'digraph {{\n{formatted_edges}\n}}'
    # G = pgv.AGraph(graph, strict=True, rankdir="LR")
    # G.layout(prog='dot')
    # G.draw(join(competition_folder, 'evidence_graph.png'))


def get_chal_path_lookup(chals_folder):

    chal_path_lookup = {}
    comp_chals = [d for d in os.listdir(
        chals_folder) if os.path.isdir(join(chals_folder, d))]
    if 'chal_host' in comp_chals:
        comp_chals.remove('chal_host')
    for comp_chal in comp_chals:
        chal_path = join(chals_folder, comp_chal)
        chal_config = join(chal_path, 'chal.yaml')
        try:
            assert os.path.exists(chal_config)
        except Exception as e:
            print(chal_config)
            raise e

        chal = load_chal_from_config(challenge_types, chal_config)
        if type(chal) is str:
            logger.error(
                "Unable to deserialize config, is the challenge bang name correct?")
            return

        chal_path_lookup[chal.name] = chal_path
    return chal_path_lookup


def get_chal_lookup(chals_folder):
    chal_lookup = {}
    comp_chals = [d for d in os.listdir(
        chals_folder) if os.path.isdir(join(chals_folder, d))]
    if 'chal_host' in comp_chals:
        comp_chals.remove('chal_host')
    for comp_chal in comp_chals:
        chal_path = join(chals_folder, comp_chal)
        chal_config = join(chal_path, 'chal.yaml')

        assert os.path.exists(chal_config)

        chal = load_chal_from_config(challenge_types, chal_config)
        if type(chal) is str:
            logger.error(
                "Unable to deserialize config, is the challenge bang name correct?")
            return

        chal_lookup[chal.name] = {
            "path": chal_path,
            "chal": chal,
        }
    return chal_lookup


def print_env_vars():
    env_vars = [
        'DOCKER_TLS_VERIFY',
        'DOCKER_HOST',
        'DOCKER_CERT_PATH',
        'MINIKUBE_ACTIVE_DOCKERD'
    ]
    for env_var in env_vars:
        env_val = os.environ.get(env_var)
        if env_val is None:
            logger.error(
                f"{env_var} is not defined! Please run `minikube start` and then `eval $(minikube -p minikube docker-env)`")
            exit(1)
        logger.info(f"{env_var}={env_val}")


def create_lock(competition_folder, chal_lookup, chal_trees):
    lock_json = {}
    display_ports = []

    def traverse(tree):
        name = tree['name']
        chal = tree['chal']
        lock_json[name] = {}
        lock_json[name]['hash'] = get_challenge_hash(chal_lookup[name], chal)
        if chal.container_id:
            lock_json[name]['container_id'] = chal.container_id
            lock_json[name]['target_port'] = chal.target_port
            lock_json[name]['display'] = chal.display
            display_ports.append(chal.display_port)
        elif 'display' in chal.__dict__:
            lock_json[name]['display'] = chal.display
        elif 'chal_file' in chal.__dict__:
            lock_json[name]['chal_file'] = chal.chal_file
        if 'children' not in tree or tree['children'] == []:
            return

        for child in tree['children']:
            traverse(child)

    for tree in chal_trees:
        traverse(tree)

    lock_json['display_ports'] = display_ports

    with open(join(competition_folder, 'challenges-lock.json'), 'w') as f:
        json.dump(lock_json, f, indent=4)


def create_ctfg(comp_folder, reg_url, admin_email, admin_password, local):
    ctfg_folder = join(comp_folder, 'ctfg')
    template_dir = join('competition_infra', 'xctf_kube')

    if os.path.exists(ctfg_folder):
        shutil.rmtree(ctfg_folder)
    shutil.copytree(template_dir, ctfg_folder)

    image = 'ctfg'
    out_port = 8000
    type = 'LoadBalancer'
    policy = 'Never'
    with WorkDir(join('competition_infra', 'xctf')), Status('[cyan] Building [bold]CTFg[/bold]', spinner_style="cyan"):
        if local:
            subprocess.check_output(
                'docker build  --platform linux/amd64 -q -t ctfg:latest .'.split())
        else:
            image = f'{reg_url}ctfg:latest'
            out_port = 80
            type = 'ClusterIP'
            policy = 'Always'
            subprocess.check_output(
                f'docker build  --platform linux/amd64 -t {reg_url}ctfg:latest -q .'.split())
            subprocess.check_output(
                f'docker push {reg_url}ctfg:latest'.split())
    fwrite(template_dir, 'ctfg-deployment.yaml', ctfg_folder, 'ctfg-deployment.yaml',
           email=admin_email, password=admin_password, image=image, policy=policy)
    fwrite(template_dir, 'ctfg-service.yaml', ctfg_folder,
           'ctfg-service.yaml', port=out_port, type=type)


@chal.command(help="Generate a challenge from a config file")
@click.pass_context
@click.option('--config', '-c', required=True)
@click.option('--competition-folder', '-f', default=None)
@click.option('--verbose', '-v', is_flag=True, default=False)
def gen(ctx, config, competition_folder, verbose):
    if verbose:
        logger.setLevel(logging.INFO)

    # print_env_vars()

    chal_dir = os.path.abspath(os.path.dirname(config))

    chal_path_lookup = {}
    chals_folder = None
    if competition_folder is not None:
        competition_folder = join(os.path.dirname(
            os.path.realpath(__file__)), competition_folder)
        chals_folder = join(competition_folder, 'chals')
        chal_path_lookup = get_chal_path_lookup(chals_folder)

    chal_gen = load_chal_from_config(challenge_types, config)
    if type(chal_gen) is str:
        logger.error(
            "Unable to deserialize config, is the challenge bang name correct?")
        return

    if chal_gen.config is None:
        logger.error("Please specify 'config' in your challenge config")
        return

    chal_tree = {}
    if ChallengeEnvironment in type(chal_gen).__bases__:
        if chals_folder == None:
            logger.error(
                "Please include the --competition-folder flag (folder where other challenges are located)")
            exit(1)
        chal_host = ChallengeHost(
            'http:/127.0.0.1:8200', chals_folder)

        chal_gen.chal_host = chal_host
        chal_gen.chal_path_lookup = chal_path_lookup
        chal_gen.challenge_types = challenge_types
        chal_tree, _ = chal_gen.gen_chals(True, '')
        chal_tree = [chal_tree]

    chal_gen.do_gen(chal_dir, True, False, None, None, '')

    if ChallengeEnvironment in type(chal_gen).__bases__:
        chal_host.create()
    if chal_tree and len(chal_tree) != 0:
        generate_challenge_graph(chal_tree, competition_folder)


def no_reg_url(ctx, param, value):
    if value:
        ctx.command.params[1].required = False
        ctx.command.params[1].default = ""
        ctx.command.params[2].required = False
        ctx.command.params[2].default = "mcpshsf.com"
    return value


@comp.command()
@click.pass_context
@click.option('--competition-folder', '-f', required=True)
@click.option('--reg-url', '-u', required=True, help="Registry to push docker images to")
@click.option('--base-url', '-b', required=True, help="Base url for the competition sites")
@click.option('--local', '-l', is_flag=True, default=False, callback=no_reg_url, help="Run the ctf locally using minikube (no reg or base url required)")
@click.option('--verbose', '-v', is_flag=True, default=False, help="Verbose logging")
@click.option('--generate-all', '-a', is_flag=True, default=False, help="Ignore lock file and generate all challenges")
def gen(ctx, competition_folder, reg_url, base_url, local, verbose, generate_all):

    if verbose:
        logger.setLevel(logging.INFO)

    if local:
        if shutil.which('minikube') is None:
            logger.error("minikube not installed!")
            return
        else:
            print_env_vars()
    else:
        try:
            subprocess.check_output(['kubectl', 'cluster-info'])
        except subprocess.CalledProcessError:
            logger.error(
                "Please set up your kubernetes cluster before running!")
            exit(1)

    with Status("[bold green]Creating challenges namespace", spinner_style="green"):
        try:
            subprocess.check_output(
                'kubectl create namespace challenges'.split())
        except subprocess.CalledProcessError:
            pass

    competition_folder = join(os.path.dirname(
        os.path.realpath(__file__)), competition_folder)
    if not os.path.exists(competition_folder):
        logger.error("Competition folder does not exist!")
        return
    chals_folder = join(competition_folder, 'chals')
    if not os.path.exists(chals_folder):
        logger.error("Chals folder does not exist!")
        return
    chal_path_lookup = get_chal_path_lookup(chals_folder)

    lock_file = join(competition_folder, 'challenges-lock.json')
    if os.path.exists(lock_file) and not generate_all:
        with open(lock_file, 'r') as f:
            chals_lock = json.load(f)
        set_used_ports(chals_lock['display_ports'])
    else:
        chals_lock = {}

    competition_config = join(competition_folder, 'config.yaml')
    assert os.path.exists(competition_config)
    yaml = ruamel.yaml.YAML()
    with open(competition_config, "r") as c:
        comp_config = yaml.load(c)

    entrypoints = comp_config['entrypoint']
    if type(entrypoints) is str:
        entrypoints = [entrypoints]

    chal_trees = []
    host_url = f'http://chal-host.chals.{base_url}'
    if local:
        host_url = 'http://127.0.0.1:8200'
        if 'CODESPACE_NAME' in os.environ.keys():
            host_url = f'https://{os.environ["CODESPACE_NAME"]}-8200.app.github.dev'
    chal_host = ChallengeHost(host_url, chals_folder)

    for entrypoint in entrypoints:
        entrypoint_path = chal_path_lookup[entrypoint]
        entrypoint_config = join(entrypoint_path, 'chal.yaml')
        chal_gen = load_chal_from_config(challenge_types, entrypoint_config)
        chal_tree = {}

        if ChallengeEnvironment in type(chal_gen).__bases__:
            chal_gen.chal_host = chal_host
            chal_gen.chal_path_lookup = chal_path_lookup
            chal_gen.challenge_types = challenge_types
            chal_tree, chals_cached = chal_gen.gen_chals(
                local, base_url, chals_lock=chals_lock)
            chal_trees.append(chal_tree)

        use_cache, attr = get_cache_state(
            chal_path_lookup, chal_gen, chals_lock)
        chal_gen.do_gen(entrypoint_path, local,
                        (use_cache and chals_cached), attr, chal_host, base_url)

        if GeneratedChallenge in type(chal_gen).__bases__:
            chal_files = chal_gen.chal_file
            if type(chal_files) is not list:
                chal_files = [chal_files]

            logger.info(chal_files)
            for chal_file in chal_files:
                chal_path = join(
                    chal_path_lookup[chal_gen.name], chal_file)
                chal_url = chal_host.add_chal(chal_path)
                logger.info(f"Generated challenge URL: {chal_url}")

    chal_host.create()
    chal_tree['host'] = chal_host
    create_lock(competition_folder, chal_path_lookup, chal_trees)

    if len(chal_trees) != 0:
        kube_dir = join(competition_folder, 'kube')
        if os.path.exists(kube_dir):
            shutil.rmtree(kube_dir)
        mkdir_p(kube_dir)

        name_to_index = {}
        entry_urls = []
        for i, config in enumerate(configs):
            name_to_index[config['name']] = i
        for entrypoint in entrypoints:
            slug = slugify(entrypoint)
            entry_url = ""
            if entrypoint in chals_lock and 'display' in chals_lock[entrypoint]:
                entry_url = chals_lock[entrypoint]['display']
            elif slug not in name_to_index.keys():
                entrypoint_path = chal_path_lookup[entrypoint]
                entrypoint_config = join(
                    entrypoint_path, 'chal.yaml')
                chal_gen = load_chal_from_config(
                    challenge_types, entrypoint_config)
                entry_url = host_url + '/' + chal_gen.get_value('file')
            else:
                entry_url = configs[name_to_index[slug]]['url']
            entry_urls.append(entry_url)

        entry_urls_str = "\n".join(entry_urls)[:-1]
        fwrite(competition_folder, comp_config['homepage'], join(
            'competition_infra', 'xctf'), 'Home.md', jinja=True, entrypoints=entry_urls_str)
        create_ctfg(competition_folder, reg_url,
                    comp_config['admin_email'], comp_config['admin_password'], local)
        configs = generate_kube_deploy(kube_dir, chal_trees, local, reg_url, base_url)
        
        with Status("[bold blue] Applying Kubernetes files", spinner="line", spinner_style="blue"):
            subprocess.check_output(
                f'kubectl apply -f {kube_dir} -n challenges'.split())
            subprocess.check_output(
                f'kubectl apply -f {join(competition_folder, "ctfg")} -n challenges'.split())
            subprocess.run(
                f'kubectl rollout restart -f {kube_dir} -n challenges'.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(
                f'kubectl rollout restart -f {join(competition_folder, "ctfg")} -n challenges'.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            generate_challenge_graph(chal_trees, competition_folder)

        full_text = "Entrypoints\n"
        for entry_url in entry_urls:
           full_text += f" - {entrypoint}: [bold][bright_white]{entry_url}[/bright_white][/bold]\n"

        ctfg_url = ""
        if local:
            if 'CODESPACE_NAME' in os.environ.keys():
                ctfg_url = f'https://{os.environ["CODESPACE_NAME"]}-8000.app.github.dev'
            else:
                ctfg_url = 'http://127.0.0.1:8000'
        else:
            ctfg_url = f'https://ctf.chals.{base_url}'

        full_text += f"\nCTFg: [bold][bright_white]{ctfg_url}[/bright_white][/bold]"

        if local:
            p = subprocess.Popen("minikube tunnel --bind-address='127.0.0.1'",
                                 stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        with Status("[bold green] Waiting for challenges to be ready", spinner_style="green"):
            ok = True
            while ok:
                ok = False
                running_output = subprocess.check_output(
                    'kubectl get pods -n challenges --no-headers'.split())
                running_pods = [line.split()[2] for line in running_output.decode(
                    'utf-8').split('\n') if len(line) > 0]
                for pod_status in running_pods:
                    if pod_status != 'Running':
                        ok = True
                        time.sleep(1)
                        break
        
        pan = Panel.fit(full_text)
        print("")
        print(pan)
        print("")

        with WorkDir(join('competition_infra', 'xctf')):
            email = comp_config['admin_email']
            password = comp_config['admin_password']
            if 'CODESPACE_NAME' in os.environ.keys():
                ctfg_url = 'http://127.0.0.1:8000'
            subprocess.run(
                f'go run main.go --url {ctfg_url}/api --email {email} --password {password} flags sync {competition_folder}/chals', shell=True, capture_output=(not verbose))

        if local:
            with Status("Running [bright_white italic]minikube tunnel --bind-address='127.0.0.1'[/bright_white italic] (press any key to stop)", spinner="point", spinner_style="bright_white"):
                input()
            os.kill(p.pid, signal.SIGSTOP)


@chalgen.command(help="Print the flags for a competition")
@click.pass_context
@click.option('--competition-folder', '-f', required=True)
def flags(ctx, competition_folder):
    competition_folder = join(os.path.dirname(
        os.path.realpath(__file__)), competition_folder)
    chals_folder = join(competition_folder, 'chals')

    chal_lookup = get_chal_lookup(chals_folder)
    for name, chal_info in chal_lookup.items():
        chal = chal_info["chal"]
        chal_path = chal_info["path"]
        print(name + ": " + chal.flag + f" ({chal_path})")


@chal.command(help="Run a challenge locally")
@click.pass_context
@click.option('--config', '-c', required=True)
def run(ctx, chal_config):
    chal_dir = os.path.dirname(chal_config)
    p = subprocess.Popen(['make', 'run'], cwd=chal_dir)
    p.wait()


@chal.command()
@click.pass_context
@click.option('--config', '-c', required=True)
def solve(ctx, chal_config):
    chal_gen = load_chal_from_config(challenge_types, chal_config)
    if chal_gen.config is None:
        logger.error("Please specify 'config' in your challenge config")
        return

    chal_dir = os.path.dirname(chal_config)
    solved_flag = chal_gen.solve(chal_dir)
    if solved_flag == chal_gen.flag:
        logger.info("Challenge is solvable")
    else:
        logger.error(
            "Challenge was not solved correctly: {}".format(solved_flag))


@chalgen.command(help="Launch a GUI for creating a competition")
@click.pass_context
@click.option('--competition-folder', '-f', required=True)
def gui(ctx, competition_folder):
    from gui import App
    App(competition_folder).mainloop()


chalgen.add_command(comp)
chalgen.add_command(chal)

if __name__ == '__main__':
    chalgen()
