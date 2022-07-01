from python:2.7.17-buster

RUN mkdir /facebook
WORKDIR /facebook

ADD app/requirements.txt /facebook/requirements.txt
RUN pip install -r requirements.txt

ADD app/fb /facebook/fb
ADD app/purepython /facebook/purepython
ADD app/manage.py /facebook/manage.py

ENV READ_ONLY true

# NON-CACHED UPDATES

ADD app/db.sqlite3 /facebook/db.sqlite3

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
