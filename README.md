[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=master&repo=593061685&machine=basicLinux32gb&devcontainer_path=.devcontainer%2Fdevcontainer.json&location=EastUs)

# chalgen

chalgen generates challenges and evidence for CTFs using a tree based format

## Past Competitions

| Competition | Writeup | Source Code |
| --- | --- | --- |
| MCPS HSF 2023 | [Writeup](https://justluk.dev/posts/writeups/mcpshsf/) | [Source Code](/competitions/mcpshsf-2023/) |

## Prerequisites
Note: This is **not required** for Github Codespaces. Everything will be installed automatically.

- Follow the documentation [here](https://pygraphviz.github.io/documentation/stable/install.html) to install `pygraphviz` for your system
- Install ffmpeg from [here](https://ffmpeg.org/download.html)
- Install Docker from [here](https://docs.docker.com/engine/install/)
- Install kubectl from [here](https://kubernetes.io/docs/tasks/tools/)
- Install minikube from [here](https://minikube.sigs.k8s.io/docs/start/) (only required for local testing)
- Install python3 from [here](https://www.python.org/downloads/)
- Install go from [here](https://golang.org/doc/install)
```
pip install -r requirements.txt
```

## Simple Usage

Run the application:

```
python chalgen.py --help
```

Example challenge generator command

```
python main.py chal gen -c tests/test_ctf/base64/chal.yaml
```

For a more detailed explanation of the commands available, see our [docs](docs/README.md).

## Todos
We have some TODOs [here](TODO.md). These are challenge ideas we have not implemented yet.
