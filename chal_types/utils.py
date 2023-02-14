import logging
from rich.logging import RichHandler
from os.path import join
from jinja2 import Template
import ruamel.yaml
from gtts import gTTS
import os


class WorkDir(object):
    def __init__(self, chal_dir):
        self.chal_dir = chal_dir
        self.cwd = os.getcwd()

    def __enter__(self):
        os.chdir(self.chal_dir)

    def __exit__(self, *args):
        os.chdir(self.cwd)


def load_chal_from_config(challenge_types, chal_config):
    yaml = ruamel.yaml.YAML()
    for chal_name, chal_type in challenge_types.items():
        yaml.register_class(chal_type)

    with open(chal_config, "r") as c:
        parsed_chals = yaml.load(c)

    if len(parsed_chals) == 1:
        return parsed_chals[0]
    else:
        raise Exception("Unable to parse challenge config")


def text_to_wav(text, path, tld='com'):
    tts = gTTS(text=text, lang='en', tld=tld)
    tts.save(path)


def fwrite(src, src_file, dest, dest_file, jinja=False, **formats):
    with open(join(src, src_file), 'r') as s, open(join(dest, dest_file), 'w') as d:
        if jinja:
            d.write(Template(s.read()).render(**formats))
        else:
            d.write(s.read().format(**formats))


class FixMinikube(object):
    def __init__(self):
        self.env_vars = ['DOCKER_TLS_VERIFY', 'DOCKER_HOST',
                         'DOCKER_CERT_PATH', 'MINIKUBE_ACTIVE_DOCKERD']
        self.env_vars_value = {'DOCKER_TLS_VERIFY': '', 'DOCKER_HOST': '',
                               'DOCKER_CERT_PATH': '', 'MINIKUBE_ACTIVE_DOCKERD': ''}
        if 'MINIKUBE_ACTIVE_DOCKERD' in os.environ:
            self.minikube_active = True
        else:
            self.minikube_active = False

    def __enter__(self):
        if self.minikube_active:
            for env_var in self.env_vars:
                self.env_vars_value[env_var] = os.environ.get(env_var)
                os.environ.pop(env_var, None)

    def __exit__(self, *args):
        if self.minikube_active:
            for env_var in self.env_vars:
                os.environ[env_var] = self.env_vars_value[env_var]

logging.basicConfig(
    level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)
log = logging.getLogger("rich")

class logger(object):
    def info(message):
        log.info(message)
    
    def error(self, message):
        log.error(message)