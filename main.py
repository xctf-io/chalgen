import logging
import subprocess
import os
import ruamel.yaml
import pygraphviz as pgv
import shutil

from slugify import slugify

from chal_types import challenge_types, load_chal_from_config, chal_to_kube_config, gen_kube, mkdir_p, logger, increase_display_port
from chal_types import GeneratedChallenge, ChallengeHost, ChallengeEnvironment
from chal_types.web import TemplateInjection
from gui import App

import rich_click as click
from rich import print
from rich.status import Status
from rich.markdown import Markdown
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

def generate_kube_deploy(kube_dir, trees, local, reg_url):
    configs = []
    port_num = 8000
    for tree in trees:
        def traverse(tree):
            if 'children' not in tree:
                return []

            kube_configs = []
            for child in tree['children']:
                chal = child['chal']
                if chal.container_id:
                    nonlocal port_num
                    kube_config = chal_to_kube_config(chal, reg_url, local, port_num, isinstance(chal, TemplateInjection))
                    port_num += 1
                    kube_configs.append(kube_config)

                kube_configs.extend(traverse(child))
            return kube_configs

        chal = tree['chal']
        if chal.container_id:
            kube_config = chal_to_kube_config(chal, reg_url, local, port_num, isinstance(chal, TemplateInjection))
            port_num += 1
            configs.append(kube_config)

        chal = tree.get('host')
        if chal and chal.container_id:
            kube_config = chal_to_kube_config(chal, reg_url, local, 8200, isinstance(chal, TemplateInjection))
            configs.append(kube_config)

        configs.extend(traverse(tree))

    gen_kube(kube_dir, configs, local)

    with Status("[bold blue] Applying Kubernetes files", spinner="line", spinner_style="blue"):
        for kube_config in os.listdir(kube_dir):
            kube_config_path = os.path.join(kube_dir, kube_config)
            subprocess.check_output(f'kubectl apply -f {kube_config_path} -n challenges'.split())

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
        if(tree['children'] == []):
            edges.append(f'\t"{tree["name"]}";')
        else:
            edges.extend(traverse(tree))

    formatted_edges = "\n".join(edges)
    graph = f'digraph {{\n{formatted_edges}\n}}'
    G = pgv.AGraph(graph, strict=True, rankdir="LR")
    G.layout(prog='dot')
    G.draw(os.path.join(competition_folder, 'evidence_graph.png'))


def get_chal_path_lookup(chals_folder):
    chal_host_folder = os.path.join(chals_folder, 'chal_host')
    if os.path.exists(chal_host_folder):
        shutil.rmtree(chal_host_folder)

    chal_path_lookup = {}
    comp_chals = [d for d in os.listdir(
        chals_folder) if os.path.isdir(os.path.join(chals_folder, d))]
    for comp_chal in comp_chals:
        chal_path = os.path.join(chals_folder, comp_chal)
        chal_config = os.path.join(chal_path, 'chal.yaml')
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
    chal_host_folder = os.path.join(chals_folder, 'chal_host')
    if os.path.exists(chal_host_folder):
        shutil.rmtree(chal_host_folder)

    chal_lookup = {}
    comp_chals = [d for d in os.listdir(
        chals_folder) if os.path.isdir(os.path.join(chals_folder, d))]
    for comp_chal in comp_chals:
        chal_path = os.path.join(chals_folder, comp_chal)
        chal_config = os.path.join(chal_path, 'chal.yaml')
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
            logger.error(f"{env_var} is not defined! Please run `minikube start` and then `eval $(minikube -p minikube docker-env)`")
            exit(1)
        logger.info(f"{env_var}={env_val}")


@chal.command(help="Generate a challenge from a config file")
@click.pass_context
@click.option('--config', '-c', required=True)
@click.option('--competition-folder', '-f', default=None)
@click.option('--verbose', '-v', is_flag=True, default=False)
def gen(ctx, chal_config, competition_folder, verbose):
    if verbose:
        logger.setLevel(logging.INFO)

    print_env_vars()

    chal_dir = os.path.abspath(os.path.dirname(chal_config))

    chal_path_lookup = {}
    chals_folder = None
    if competition_folder is not None:
        competition_folder = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), competition_folder)
        chals_folder = os.path.join(competition_folder, 'chals')
        chal_path_lookup = get_chal_path_lookup(chals_folder)

    chal_gen = load_chal_from_config(challenge_types, chal_config)
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
            logger.error("Please include the --competition-folder flag (folder where other challenges are located)")
            exit(1)
        chal_host = ChallengeHost(
            'http://chal-host.chals.mcpshsf.com', chals_folder)

        chal_gen.chal_host = chal_host
        chal_gen.chal_path_lookup = chal_path_lookup
        chal_gen.challenge_types = challenge_types
        chal_tree = chal_gen.gen_chals(chal_dir, local=True)
        chal_tree = [chal_tree]

    chal_gen.do_gen(chal_dir, local=True)

    if ChallengeEnvironment in type(chal_gen).__bases__:
        chal_host.create()
    if chal_tree and len(chal_tree) != 0:
        generate_challenge_graph(chal_tree, competition_folder)


def no_reg_url(ctx, param, value):
    if value:
        ctx.command.params[1].required = False
        ctx.command.params[1].default = ""
    return value

@comp.command()
@click.pass_context
@click.option('--competition-folder', '-f', required=True)
@click.option('--reg-url', '-r', required=True, help="Registry to push docker images to")
@click.option('--local', '-l', is_flag=True, default=False, callback=no_reg_url, help="Run the ctf locally using minikube (no reg url required)")
@click.option('--verbose', '-v', is_flag=True, default=False)
def gen(ctx, competition_folder, reg_url, local, verbose):
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
            logger.error("Please set up your kubernetes cluster before running!")
            exit(1)
    try:
        with Status("[bold green]Creating challenges namespace", spinner_style="green"):
            subprocess.check_output('kubectl create namespace challenges'.split())
    except subprocess.CalledProcessError:
        pass
    competition_folder = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), competition_folder)
    chals_folder = os.path.join(competition_folder, 'chals')

    chal_path_lookup = get_chal_path_lookup(chals_folder)

    competition_config = os.path.join(competition_folder, 'config.yaml')
    assert os.path.exists(competition_config)

    yaml = ruamel.yaml.YAML()
    with open(competition_config, "r") as c:
        comp_config = yaml.load(c)

    entrypoints = comp_config['entrypoint']

    if type(entrypoints) is str:
        entrypoints = [entrypoints]

    chal_trees = []
    host_url = 'http://chal-host.chals.mcpshsf.com'
    if local:
        host_url = 'http://127.0.0.1.:8200'
        if 'CODESPACE_NAME' in os.environ.keys():
            host_url = f'https://{os.environ["CODESPACE_NAME"]}-8200.preview.app.github.dev'
    chal_host = ChallengeHost(host_url, chals_folder)

    entry_files = {}
    for entrypoint in entrypoints:
        entrypoint_path = chal_path_lookup[entrypoint]
        entrypoint_config = os.path.join(entrypoint_path, 'chal.yaml')
        chal_gen = load_chal_from_config(challenge_types, entrypoint_config)
        chal_tree = {}
        increase_display_port()

        if ChallengeEnvironment in type(chal_gen).__bases__:
            chal_gen.chal_host = chal_host
            chal_gen.chal_path_lookup = chal_path_lookup
            chal_gen.challenge_types = challenge_types
            chal_tree = chal_gen.gen_chals(entrypoint_path, local=local)
            chal_trees.append(chal_tree)

        chal_gen.do_gen(entrypoint_path, local=local)

        if GeneratedChallenge in type(chal_gen).__bases__:
            chal_files = chal_gen.chal_file
            if type(chal_files) is not list:
                chal_files = [chal_files]

            logger.info(chal_files)
            for chal_file in chal_files:
                chal_path = os.path.join(
                    chal_path_lookup[chal_gen.name], chal_file)
                chal_url = chal_host.add_chal(chal_path)
                logger.info(f"Generated challenge URL: {chal_url}")

    chal_host.create()
    chal_tree['host'] = chal_host

    if len(chal_trees) != 0:
        kube_dir = os.path.join(competition_folder, 'kube')
        mkdir_p(kube_dir)
        configs = generate_kube_deploy(kube_dir, chal_trees, local, reg_url)
        generate_challenge_graph(chal_trees, competition_folder)
        
        name_to_index = {}
        for i, config in enumerate(configs):
            name_to_index[config['name']] = i
        full_text  = "Entrypoints\n"
        for entrypoint in entrypoints:
            slug = slugify(entrypoint)
            entry_url = ""
            if slug not in name_to_index.keys():
                entrypoint_path = chal_path_lookup[entrypoint]
                entrypoint_config = os.path.join(entrypoint_path, 'chal.yaml')
                chal_gen = load_chal_from_config(challenge_types, entrypoint_config)
                entry_url = host_url + '/' + chal_gen.get_value('files')[0]
            else:
                entry_url = configs[name_to_index[slug]]['url']
            full_text += f" - {entrypoint}: [bold][bright_white]{entry_url}[/bright_white][/bold]\n"
        
        print("")
        if local:
            full_text += "\n[white]Run [bold][bright_red]minikube tunnel --bind-address='127.0.0.1'[/bright_red][/bold] to access everything. You may need to restart the tunnel if it fails to connect.[/white]"
        p = Panel.fit(full_text)    
        print(p)
            

@chalgen.command(help="Print the flags for a competition")
@click.pass_context
@click.option('--competition-folder', '-f', required=True)
def flags(ctx, competition_folder):
    competition_folder = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), competition_folder)
    chals_folder = os.path.join(competition_folder, 'chals')

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
    App(competition_folder).mainloop()

chalgen.add_command(comp)
chalgen.add_command(chal)

if __name__ == '__main__':
    chalgen()
