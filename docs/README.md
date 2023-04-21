Chalgen Docs
==============
## Links
  - [All challenges](chal_types/README.md)
  - [Concepts explained](README.md#concepts-explained)
  - [Example commands](README.md#available-commands)
  - [Running on AWS](README.md#run-a-competition-on-an-aws-lab)

## Concepts explained

### Challenges
A challenge is represented by a YAML file like the following:

```yaml
- !ext4_file_recovery
  name: "Ext4 File Recovery"
  flag: "flag{this_is_a_test}"
  config:
    deleted_evidence: evidence
    fluff: fluff
```

The type of challenge is determined by the YAML tag (starts with a !). Values in the `config` field allow you customize the challenge to your competition.

### Challenge environments
Challenge environments host other challenges and can also be configured to fit the competition. They have the same fields as Challenges but also "link" to other challenges through the `chals` subfield. An example is shown below.

```yaml
- !jekyll_blog
  name: Jekyll Blog
  flag: "flag{test}"
  config:
    meta:
      title: Chance's Cooking Blog!
    posts:
    - 2014-06-08-post1.md
    - 2014-06-08-post2.md
    chals:
      - Vigenere
      - Docx Carving
```

Challenges link through the `name` field. Challenge environments can't be made/run through the `python main.py gen` command, so you must use `python main.py comp gen`. 

### Competition structure
Competitions are structured in a tree-like fashion, with some Challenge Environments serving as entrypoints. An example structure is shown below. In this case, Fesbuc is an entrypoint.

![image](../competitions/mcpshsf-2023/evidence_graph.png)

A competition folder has a `config.yaml` that specifies the entrypoints and `chals` folder that contains the challenges. You can look at the example in [/competitions/middle-school-teaser-2021](/competitions/middle-school-teaser-2021/)

## Available commands
***
### Run the Competion Creator GUI

```shell
python main.py gui -f <relative path of the competition folder>
```

After running the above command, a GUI will pop up to help scaffold your competition. You can create a challenge map and after clicking 
create competition files, a folder with all the nessecary YAML files will be created. You cab edit these YAML file to customize your competition.
***
### Generate a single challenge

```shell
python main.py chal gen -c <relative path of the challenge YAML>
```

This command generates all the files for challenges and builds the docker image if needed.
***
### Run a single challenge

```shell
python main.py chal run -c <relative path of the challenge YAML>
```

This command runs the docker image for local testing. You must run `python main.py chal gen` before in order to create all the files and build.
***
### Build a competition for Kubernetes

```shell
python main.py comp gen -f <relative path of the competition> -r <registry to push images to>
```

This command builds all of the Kubernetes files needed to deploy to a prexisting Kubernetes cluster. Upon completion, a graph of the challenges will be generated. The graph will be located at `evidence_graph.png` file in the competition folder.

### Build and run a competition locally

```shell
python main.py comp gen -f <relative path of the competition> -l
```

This command assumes you have `minikube` installed. Install it [here](https://minikube.sigs.k8s.io/docs/start/). This command runs the competition using minikube for local testing. Remember to add `127.0.0.1:53` as a DNS server. The urls of the challenges will be located in the `zones.txt` file.
***

## Run a competition on an AWS Lab

 - Start by running the competitiongen command, as shown [above](README.md#build-a-competition-for-kubernetes) (for Kubernetes)
    - Choose `docker.io/<your username>/` for a free, public registry
 - Paste `curl https://gist.githubusercontent.com/just-luk/d5e2dbf530d2d162e853d356cfe0a792/raw/run.sh | bash` into the Lab terminal
 - Wait for your instances to start
 - Run `export KUBECONFIG=./kubeconfig` to use the kube config
    - Rerun everytime you refresh
 - Transfer all files in the `kube` directory to the Lab
 - Run `kubectl create namespace challenges`
 - Change the annotation field of ingress.yaml to `traefik.ingress.kubernetes.io/router.entrypoints: web`
 - Run `kubectl apply -f kube` to start the competition
 - Run `aws lightsail open-instance-public-ports --instance-name "Agent1" --port-info fromPort=80,toPort=80`
    - The static ip address of Agent1 will be the ingress
 - Stop the competition with `kubectl delete namespace challenges`

