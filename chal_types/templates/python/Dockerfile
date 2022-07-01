FROM python:3.9.6-alpine
WORKDIR /app
RUN pip3 install {requirements}
COPY app .
RUN adduser -D web
RUN chmod -R 755 . 
RUN chmod 1733 /tmp /var/tmp /dev/shm
USER web
CMD [ "python3", "main.py"]