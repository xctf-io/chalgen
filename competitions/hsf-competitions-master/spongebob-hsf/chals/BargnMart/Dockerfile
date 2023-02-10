FROM nginx:alpine

ENV webroot /usr/share/nginx/html

COPY root $webroot/
COPY chals/output.wav $webroot/
COPY chals/access.log $webroot/
