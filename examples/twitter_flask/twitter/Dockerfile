from python:2.7.17-buster

WORKDIR /twitter
ADD . /twitter

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "run.py"]