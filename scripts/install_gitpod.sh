sudo apt-get -y update
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt-get update
sudo apt-get -y install google-cloud-sdk
sudo apt-get -y install graphviz libgraphviz-dev ffmpeg google-cloud-sdk-gke-gcloud-auth-plugin kubectl
pip install pygraphviz 
pip install -r requirements.txt
git clone https://github.com/xctf-io/xctf competition_infra/xctf
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
rm minikube_latest_amd64.deb