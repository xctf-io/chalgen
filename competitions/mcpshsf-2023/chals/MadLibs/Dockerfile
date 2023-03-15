# Modified from kctf https://github.com/google/kctf
FROM python:3.8-slim as chroot

RUN /usr/sbin/useradd -u 1000 user
RUN apt-get update && \
    apt-get install -yq socat libev-dev gcc && \
    rm -rf /var/lib/apt/lists/*

RUN pip install Flask bjoern --no-cache-dir

COPY app /app
COPY run.sh run.sh
RUN sed -i 's/\r//' run.sh

FROM gcr.io/kctf-docker/challenge@sha256:56f7dddff69d08d4d19f4921c724d438cf4d59e434c601f9776fd818368b7107

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends apache2 \
    && rm -rf /var/lib/apt/lists/*

RUN service apache2 start

COPY --from=chroot / /chroot

# For Proxy
RUN ln -s /etc/apache2/mods-available/proxy.load /etc/apache2/mods-enabled/
RUN ln -s /etc/apache2/mods-available/proxy_http.load /etc/apache2/mods-enabled/

COPY apache2-nsjail.conf /etc/apache2/conf-enabled/

COPY nsjail.cfg /home/user/nsjail.cfg

VOLUME /var/log/apache2
VOLUME /var/run/apache2

CMD kctf_setup \
    && (kctf_drop_privs nsjail --config /home/user/nsjail.cfg --port 8081 -- /bin/bash run.sh &) \
    && bash -c 'source /etc/apache2/envvars && APACHE_RUN_USER=user APACHE_RUN_GROUP=user /usr/sbin/apache2 -D FOREGROUND'
