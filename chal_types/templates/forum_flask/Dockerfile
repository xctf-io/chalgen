FROM python:2.7-alpine
RUN apk update && \
    apk add python python-dev linux-headers libffi-dev gcc make musl-dev py-pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /opt/forum
VOLUME ["/opt/forum"]

EXPOSE 3005

CMD ["gunicorn", "forum.forum:app"]