sudo apt -y update
sudo apt -y install graphviz graphviz-dev ffmpeg google-cloud-sdk-gke-gcloud-auth-plugin kubectl
pip install pygraphviz 
pip install -r requirements.txt
git clone https://github.com/xctf-io/xctf competition_infra/xctf
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
rm minikube_latest_amd64.deb

