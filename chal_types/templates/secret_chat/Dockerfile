FROM python:3.10.4-slim-buster
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py
RUN rm manage.py
CMD waitress-serve --host 0.0.0.0 --port 5000 routes:app