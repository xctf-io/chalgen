[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=master&repo=593061685&machine=basicLinux32gb&devcontainer_path=.devcontainer%2Fdevcontainer.json&location=EastUs)

# chalgen

chalgen generates challenges which are nodes in an evidence map

## Past Competitions

| Competition | Writeup | Source Code |
| --- | --- | --- |
| MCPS HSF 2023 | [Writeup](https://lukegriffith.me/posts/writeups/mcpshsf/) | [Source Code](/competitions/mcpshsf-2023/) |

## Prerequisites

- Follow the documentation [here](https://pygraphviz.github.io/documentation/stable/install.html) to install `pygraphviz` for your system
- Install ffmpeg from [here](https://ffmpeg.org/download.html)
- Install Docker from [here](https://docs.docker.com/engine/install/)
- Install kubectl from [here](https://kubernetes.io/docs/tasks/tools/)

## Basic setup

Install the requirements:

```
pip install -r requirements.txt
```

Run the application:

```
python chalgen.py --help
```

Example challenge generator command

```
python chalgen.py gen --chal-config tests/test_ctf/base64/chal.yaml
```

To run the tests:

```
pytest
```

## Evidence Guidelines

* A challenge may provide an option to include data within it to make it story relevant
* A challenge is expected to be solvable by itself. If a challenge is not solvable by itself (i.e. encrypted zip has unguessable password), then a connection must be specified for the challenge.
* Challenges may specify a way to embed another challenge inside of themselves.

Some questions that should be answered:

* How much perscription do we want to give challenges?
* If we are creating an sql injection challenge, do we give them website and the vuln code?
* Need to figure out how the vuln plugs into a website. Have a module system for the website that you drop in views for challenges.