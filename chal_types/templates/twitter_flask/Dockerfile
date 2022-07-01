FROM python:2.7.17-buster as builder
ADD project /project
ADD requirements.txt /
ADD db_create.py /
RUN pip install -r requirements.txt
RUN python db_create.py

FROM python:2.7.17-buster

WORKDIR /twitter

ADD requirements.txt /twitter
RUN pip install -r requirements.txt

ADD run.py /twitter
ADD project/dms /twitter/project/dms
ADD project/static /twitter/project/static
ADD project/templates /twitter/project/templates
ADD project/tweets /twitter/project/tweets
ADD project/users /twitter/project/users
ADD project/__init__.py /twitter/project/__init__.py
ADD project/_config.py /twitter/project/_config.py
ADD project/models.py /twitter/project/models.py

ENV READ_ONLY true

# NON-CACHED CHANGES
COPY --from=builder project/database.db project/database.db

EXPOSE 5000
CMD ["python", "run.py"]