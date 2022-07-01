FROM python:2.7-alpine
RUN apk update && \
    apk add python python-dev linux-headers libffi-dev gcc make musl-dev py-pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /opt/forum
VOLUME ["/opt/forum"]
WORKDIR /opt/forum

ENV FS_USERNAME '{username}'
ENV FS_PASSWORD '{password}'

# NON-CACHED UPDATES

{setup}

EXPOSE 8000

CMD ["gunicorn", "file_server:app", "--bind", "0.0.0.0:8000"]