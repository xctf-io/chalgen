Chalgen Docs
==============


## Available Commands
***
### Run the Competion Creator GUI

```shell
python chalgen.py gui --competition-folder=<relative path of the competition folder>
```

After running the above command, a GUI will pop up to help scaffold your competition. You can create a challenge map and after clicking 
create competition files, a folder with all the nessecary YAML files will be created. You cab edit these YAML file to customize your competition.
***
### Generate a single challenge

```shell
python chalgen.py gen --chal-config=<relative path of the challenge YAML>
```

This command generates all the files for challenges and builds the docker image if needed.
***
### Run a single challenge

```shell
python chalgen.py run --chal-config=<relative path of the challenge YAML>
```

This command runs the docker image for local testing. You must run `python chalgen.py gen` before in order to create all the files and build.
***
### Build a competition for Kubernetes

```shell
python chalgen.py competitiongen --competition-folder=<relative path of the competition> --reg-url=<registry to push images to>
```

This command builds all of the Kubernetes files needed to deploy to a Kubernetes cluster. 
***
### Build and run a competition locally

```shell
python chalgen.py competitiongen --competition-folder=<relative path of the competition> --local
```

This command assumes you have `minikube` installed. Install it [here](https://minikube.sigs.k8s.io/docs/start/). This command runs the competition using minikube for local testing. Remember to add `127.0.0.1:53` as a DNS server. The urls of the challenges will be located in the `zones.txt` file.
***
