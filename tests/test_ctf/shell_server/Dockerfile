FROM dit4c/gotty

RUN adduser test_user -D
ADD root /

CMD ["--credential", "username:password", "--permit-write", "--reconnect", "/bin/sh"]
