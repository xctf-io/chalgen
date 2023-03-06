FROM python:3.10.4-slim-buster as build
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py
RUN rm manage.py
CMD gunicorn --workers 4 --bind 0.0.0.0:5000 routes:app