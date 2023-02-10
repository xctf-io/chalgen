FROM python:2.7-alpine
RUN apk update && \
    apk add python python-dev linux-headers libffi-dev gcc make musl-dev py-pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /opt/forum
VOLUME ["/opt/forum"]
WORKDIR /opt/forum

ENV FS_USERNAME 'k4r5t_t0p0gr4phy'
ENV FS_PASSWORD 'y4z00_tr1but4ry'

# NON-CACHED UPDATES



EXPOSE 8000

CMD ["gunicorn", "file_server:app", "--bind", "0.0.0.0:8000"]