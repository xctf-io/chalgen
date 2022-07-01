FROM cthompson4321/gotty:v0.0.1

RUN adduser fred -D && adduser daisy -D
ADD root /

WORKDIR /home/Daisy
CMD ["--credential", "daisy:I<3computers", "--permit-write", "--reconnect", "/bin/sh"]
