FROM accetto/ubuntu-vnc-xfce-firefox-g3
USER 0
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -yq --no-install-recommends exiftool wget wireshark ruby mousepad
RUN gem install zsteg
RUN echo "headless ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER 1000
