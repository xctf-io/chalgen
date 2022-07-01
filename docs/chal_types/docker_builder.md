Module chal_types.docker_builder
================================

Classes
-------

`DockerBuilder(name=UUID('5c5f1207-5ac4-4a61-9c6a-0442d47dddbc'), base_img='scratch', input_dir='input', included_files=[], output_files=[], outdir=None)`
:   

`DockerNetwork(containers: list, outdir: str, docker_outputs: dict)`
:   

`Process(shell)`
:   

```
Methods:
    - clone(self)
    - run(self, cmd, wait=True, timeout=600, detach=True)
```

`WorkDir(chal_dir)`
: