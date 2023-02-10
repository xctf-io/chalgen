import errno
import os
import sys
import ruamel.yaml
from shutil import copyfile, copytree, rmtree
from os.path import join, abspath, dirname
from slugify import slugify
from .utils import WorkDir, logger

yaml = ruamel.yaml.YAML()


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def get_kube_service(chal, namespace='challenges'):
    chal_name = chal['name']
    service_name = chal['service_name']
    target_port = chal['target_port']
    out_port = chal['out_port']
    return {
        'apiVersion': 'v1',
        'kind': 'Service',
        'metadata': {
            'name': service_name,
            'namespace': namespace,
            'labels': {
                'app': chal_name
            }
        },
        'spec': {
            'type': 'LoadBalancer',
            'ports': [
                {
                    'port': out_port,
                    'targetPort': target_port,
                    'protocol': 'TCP'
                }
            ],
            'selector': {
                'app': chal_name
            }
        }
    }


def get_kube_deployment(chal, local, namespace='challenges'):
    chal_name = chal['name']
    chal_security = chal['security']
    service_name = chal['service_name']
    registry_url = chal['registry_url']

    spec = {
        # 'securityContext': {
        #     'runAsUser': 1000,
        #     'runAsGroup': 3000,
        #     'fsGroup': 2000,
        # },
        'containers': [{
            'name': chal_name,
            'image': registry_url,
            'ports': [
                {
                    'containerPort': chal['target_port']
                }
            ],
            'imagePullPolicy': 'Always',
            'securityContext': {
                'readOnlyRootFilesystem': chal_security == 'readonly'
            }
        }],
        'imagePullSecrets': [{
            'name': 'regcred'
        }]
    }
    if local:
        spec['containers'][0]['imagePullPolicy'] = 'Never'
        spec['containers'][0]['securityContext'] = {
            'allowPrivilegeEscalation': False, 'runAsUser': 0}
    return {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {
            'name': service_name,
            'namespace': namespace,
            'labels': {
                'app': chal_name
            }
        },
        'spec': {
            'replicas': 1,
            'selector': {
                'matchLabels': {
                    'app': chal_name
                }
            },
            'template': {
                'metadata': {
                    'labels': {
                        'app': chal_name
                    }
                },
                'spec': spec
            }
        }
    }


def get_kube_ingress(chals, namespace='challenges'):
    rules = []
    for chal in chals:
        service_name = chal['service_name']
        url = chal['url']
        out_port = chal['out_port']
        rules.append({
            'host': url,
            'http': {
                'paths': [{
                    'pathType': 'ImplementationSpecific',
                    'path': '/',
                    'backend': {
                        'service': {
                            'name': service_name,
                            'port': {
                                'number': out_port
                            }
                        }
                    }
                }]
            }
        })

    return {
        'apiVersion': 'networking.k8s.io/v1',
        'kind': 'Ingress',
        'metadata': {
            'name': 'challenge-ingress',
            'namespace': namespace,
            'annotations': {
                'kubernetes.io/ingress.class': 'nginx',
                'nginx.ingress.kubernetes.io/ssl-redirect': 'false'
            }
        },
        'spec': {
            'rules': rules
        }
    }


def chal_to_kube_config(chal, registry_base_url, local):
    chal_name = slugify(chal.name)
    service_name = f'{chal_name}-svc'
    registry_url = f'{registry_base_url}{chal_name}:latest'
    url_base = 'chals.mcpshsf.com'
    out_port = 80
    if local:
        url_base = 'ctf.test'
        out_port = 8000
    url = f'{chal_name}.{url_base}'
    return {
        'name': chal_name,
        'service_name': service_name,
        'registry_url': registry_url,
        'url': url,
        'target_port': chal.target_port,
        'container_id': chal.container_id,
        'security': chal.security,
        'out_port': out_port
    }


def push_container(chal_config, local):
    os.system(
        f'docker tag {chal_config["container_id"]} {chal_config["registry_url"]}')
    if not local:
        os.system(f'docker push {chal_config["registry_url"]}')
    os.system(f'docker rmi {chal_config["container_id"]}')


def gen_kube(kube_dir, chal_kube_configs, local):
    yaml = ruamel.yaml.YAML()
    for chal_kube_config in chal_kube_configs:
        kube_config_out = os.path.join(
            kube_dir, f'{chal_kube_config["name"]}.yaml')

        service_config = get_kube_service(chal_kube_config)
        deployment_config = get_kube_deployment(chal_kube_config, local)

        with open(kube_config_out, 'w') as out:
            yaml.dump_all([service_config, deployment_config], out)

        push_container(chal_kube_config, local)

    # chal_kube_configs = [
    #     *chal_kube_configs,
    #     {
    #         "service_name": "ctfd-svc",
    #         "url": "camp.mcpshsf.com"
    #     }
    # ]
    ingress_config = get_kube_ingress(chal_kube_configs)
    kube_ingress_out = os.path.join(kube_dir, 'ingress.yaml')
    with open(kube_ingress_out, 'w') as out:
        yaml.dump(ingress_config, out)


class ChallengeHost(object):
    def __init__(self, url, chals_dir):
        self.url = url
        self.chals = []
        self.host_dir = os.path.join(chals_dir, 'chal_host')
        self.name = 'chal_host'
        self.target_port = 80
        self.security = None
        if not os.path.isdir(self.host_dir):
            os.makedirs(self.host_dir)

    def add_chal(self, file):
        self.chals.append(file)
        filename = os.path.basename(file)
        return f'{self.url}/{filename}'

    def create(self):
        template_dir = join(dirname(abspath(__file__)),
                            'templates/fileshare_nginx')
        makefile_dir = join(dirname(abspath(__file__)),
                            'templates/docker_make')

        if(os.path.isdir(self.host_dir)):
            rmtree(self.host_dir)
        copytree(template_dir, self.host_dir)

        for chal in self.chals:
            copyfile(chal, join(self.host_dir, os.path.basename(chal)))

        file_setup = "\n".join(
            [f'COPY {os.path.basename(chal)} /usr/share/nginx/html/'
                for chal in self.chals]
        )

        with open(join(template_dir, 'Dockerfile'), 'r') as template_docker,\
                open(join(self.host_dir, 'Dockerfile'), 'w') as docker:
            docker.write(template_docker.read().format(setup=file_setup))

        self.container_id = f'chal_host-{hash(self)}'
        with open(join(makefile_dir, 'Makefile'), 'r') as template_make,\
                open(join(self.host_dir, 'Makefile'), 'w') as make:
            make.write(template_make.read().format(
                chal_name=self.container_id, chal_run_options=''))

        with WorkDir(self.host_dir):
            os.system('make build')


class GeneratedChallenge(object):
    security = None

    def __init__(self, name, flag, config):
        self.name = name
        self.flag = flag
        self.evidence = "THIS IS PLACEHOLDER EVIDENCE"
        self.config = config
        self.display = "nothing to display"
        self.chal_host = None
        self.chal_dir = "not set"

    def do_gen(self, chal_dir):
        print(f'Generating {self.__class__} {self.name}')
        self.chal_dir = chal_dir
        self.container_id = None
        self.target_port = 80
        self.gen(chal_dir)

    def gen(self, chal_dir):
        # override
        pass

    def get_value(self, key, required=True):
        if key not in self.config.keys():
            if required:
                logger.error("Unable to find {} in config".format(key))
                sys.exit(-1)
            else:
                return None
        else:
            return self.config[key]

    def get_file_path(self, filename):
        return os.path.join(self.chal_dir, filename)

    def get_file(self, filename):
        with open(self.get_file_path(filename), 'rb') as f:
            return f.read()
