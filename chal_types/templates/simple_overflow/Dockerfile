from alpine:3.7

RUN apk add build-base

ADD overflow.c /app/
ADD password.txt /app/
ADD Makefile /app/

WORKDIR /app

RUN make overflow

CMD /bin/sh
