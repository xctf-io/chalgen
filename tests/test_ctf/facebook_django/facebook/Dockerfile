from python:2.7.17-buster

WORKDIR /facebook

RUN pip install -r requirements.txt

ADD app/ /facebook/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]