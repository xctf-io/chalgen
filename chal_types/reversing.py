from .challenge import GeneratedChallenge
from .docker_builder import DockerBuilder


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
    """

    Config:
        TODO: Some custom welcome message or resources
    """

    def gen(self, chal_dir):
        pass


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
