FROM python:3.6.6-jessie

MAINTAINER breadchris

ENV SRVHOME=/srv/app

WORKDIR $SRVHOME

COPY ./ $SRVHOME

RUN apt-get update && apt-get install -y \
    nginx \
    supervisor

COPY ./nginx/nginx.conf /etc/nginx/
COPY ./nginx/gunicorn-app.conf /etc/nginx/conf.d/
#COPY ./nginx/start-nginx.sh . /usr/bin/

COPY ./gunicorn_config.py /etc/gunicorn/

COPY supervisord.conf /etc/supervisor/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80
EXPOSE 8080

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

CMD ["/usr/bin/supervisord"]
