import os
from os.path import join, abspath, dirname
from shutil import copyfile
from distutils.dir_util import copy_tree
from .challenge import GeneratedChallenge
from .utils import WorkDir, fwrite
from slugify import slugify
from .ai_generation import gen_full_site

robots_format = '''User-agent: *
Disallow: {flag}
'''
robots_setup = """ADD robots.txt $webroot/robots.txt
ADD index.html $webroot/index.html
"""


class RobotsTxtChallenge(GeneratedChallenge):
    yaml_tag = u'!robots_txt'
    __doc__ = """
    Flag is located in the robots file

    Config:
    
        index - Custom index.html page
        prompt - Custom AI powered generation instructions for a website. (Ex. Make a cooking website...)
        text - Optional additional information
    """

    def gen(self, chal_dir):
        """
        TODO (breadchris) cleanup here
        - this is mostly just for getting down ideas, please refactor
        - Ideally we should be using docker compose
        - Docker templates and makefile templates should exist as helper functions
        """
        self.set_display()

        template_dir = join(dirname(abspath(__file__)),
                            'templates/static_site')
        makefile_dir = join(dirname(abspath(__file__)),
                            'templates/docker_make')
        prompt = self.get_value('prompt', required=False)
        index_page = self.get_value('index', required=False)
        text = self.get_value('text', required=False)

        # if an index.html page has not been configured, add the default one
        if index_page is None:
            copyfile(join(template_dir, 'index.html'),
                     join(chal_dir, 'index.html'))
        
        if prompt is not None:
            prompt += " Create unique text to fill the webpage. You should include css in this html file, and any image src= references should be set to a unique vivid description of what the image should be, encapsulated by []."
            gen_full_site(prompt, join(chal_dir, 'index.html'))

        with open(join(chal_dir, 'robots.txt'), 'w') as f:
            f.write(robots_format.format(flag=self.flag))
            if text is not None:
                f.write(text)

        fwrite(template_dir, 'Dockerfile', chal_dir,
               'Dockerfile', setup=robots_setup)
        self.container_id = f'robots_txt-{hash(self)}'
        fwrite(makefile_dir, 'Makefile', chal_dir, 'Makefile',
               chal_name=self.container_id, chal_run_options=f'-p 8080:{self.target_port}')

        self.build_docker(chal_dir)


class TemplateInjection(GeneratedChallenge):
    yaml_tag = u'!temp_inj'
    __doc__ = """
    Flag is located in flag.txt

    Config:

        author - author of mad lib generator
        blacklist - blackist for disallowed words(leave as [] for a blank blacklist)
        files - optional additional files to add to webroot
    """

    def gen(self, chal_dir):
        cur_file_path = dirname(abspath(__file__))
        temp_dir = join(cur_file_path, 'templates/temp_inj')
        nsjail_dir = join(cur_file_path, 'templates/nsjail_flask')
        files = self.get_value("files", required=False)
        blacklist = self.get_value("blacklist")
        author = self.get_value("author")

        self.set_display()

        app_dir = join(chal_dir, 'app')
        copy_tree(temp_dir, app_dir)
        copy_tree(nsjail_dir, chal_dir)
        if files is not None:
            for file in files:
                copyfile(join(chal_dir, file), join(app_dir, file))

        self.container_id = f'temp_inj-{hash(self)}'
        self.target_port = 8080
        fwrite(cur_file_path, 'templates/docker_make/Makefile', chal_dir, 'Makefile', chal_name=self.container_id,
               chal_run_options=f'-p 8080:{self.target_port} --cap-drop all --cap-add chown --cap-add setuid --cap-add setgid \
        --cap-add sys_admin --security-opt apparmor=unconfined --security-opt seccomp=unconfined')
        fwrite(temp_dir, 'flag.txt', app_dir, 'flag.txt', flag=self.flag)
        fwrite(temp_dir, 'main.py', app_dir, 'main.py',
               jinja=True, blacklist=blacklist)
        fwrite(temp_dir, 'templates/base.html', app_dir, 'templates/base.html', jinja=True,
               author=author, content="{% block content %}{% endblock %}")

        self.build_docker(chal_dir)
