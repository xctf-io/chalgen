from .challenge import GeneratedChallenge
from .docker_builder import DockerBuilder
import subprocess
import os
from shutil import make_archive
from .utils import WorkDir, join
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

    # def gen(self, chal_dir):
    #     java_source_file = "MyClass.java"

    #     flag = self.flag

    #     compile_command = ["javac", java_source_file]
    #     subprocess.run(compile_command, check=True)

    #     class_file = "MyClass.class"
    #     manifest_file = "Manifest.txt"

    #     manifest_content = "Main-Class: MyClass\n"
    #     with open(manifest_file, "w") as f:
    #         f.write(manifest_content)

    #     jar_file = "MyJar.jar"

    #     jar_command = ["jar", "cfm", jar_file, manifest_file, class_file]

    #     subprocess.run(jar_command, check=True)

    #     os.remove(manifest_file)
    #     os.remove(class_file)

    #     shutil.move(jar_file, chal_dir)
    def gen(self, chal_dir):
        source_file_path = '.chal_files/simple_jar_re/MyClass.java'

        stripped_flag = self.flag.replace("flag{", "").replace("}", "")

        with open(source_file_path, 'w') as f:
            data=f.read()
            data = data.replace('$FLAG$', stripped_flag)

        with WorkDir(chal_dir) as wd:

            included_files = [source_file_path]
            jar_folder = "jar_folder"
            builder = DockerBuilder(
                base_img="archlinux",
                input_dir="input",
                included_files=included_files,
                output_files=[join("/", jar_folder)],
                outdir=chal_dir
            )

            with builder as b:
                b.run("sudo apt-get install -y openjdk-8-jdk")
                b.run("javac MyClass.java")
                b.run("jar cf MyJar.jar MyClass.class")
                b.run("rm -rf MyClass.class")

            chal_zip = join(chal_dir, "chal")
            outdir = join(chal_dir, 'git_chal')
            make_archive(chal_zip, "zip", outdir)
            self.chal_file = "chal.zip"



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
