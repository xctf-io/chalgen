FROM python:2.7.17-buster as builder
ADD app /app
WORKDIR /app
RUN pip install --no-build-isolation -r requirements.txt
RUN echo no | python manage.py syncdb
RUN python manage.py loaddata fixture.yaml

FROM python:2.7.17-buster

RUN mkdir /facebook
WORKDIR /facebook

ADD app/requirements.txt /facebook/requirements.txt
RUN pip install --no-build-isolation -r requirements.txt

ADD app/fb /facebook/fb
ADD app/purepython /facebook/purepython
ADD app/manage.py /facebook/manage.py

ENV READ_ONLY true

# NON-CACHED UPDATES

COPY --from=builder app/db.sqlite3 /facebook/db.sqlite3

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
