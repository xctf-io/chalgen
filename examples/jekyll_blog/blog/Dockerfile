FROM jekyll/builder:3.8 AS builder
COPY . /srv/jekyll
RUN jekyll build

FROM nginx:alpine

COPY --from=builder /srv/jekyll/_site /usr/share/nginx/html