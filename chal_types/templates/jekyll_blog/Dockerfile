FROM klakegg/hugo:0.107.0-onbuild AS hugo

FROM nginx:1.23.3
COPY --from=hugo /target /usr/share/nginx/html
