FROM mcr.microsoft.com/devcontainers/universal

RUN sudo apt -y update
RUN sudo apt -y install graphviz graphviz-dev ffmpeg
RUN pip install pygraphviz 
RUN pip install -r requirements.txt
