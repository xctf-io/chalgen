FROM nginx:alpine

ARG TEMPLATE_SCRIPT=$TEMPLATE_SCRIPT

ADD $TEMPLATE_SCRIPT
RUN $TEMPLATE_SCRIPT

COPY index.html /usr/share/nginx/html/index.html
