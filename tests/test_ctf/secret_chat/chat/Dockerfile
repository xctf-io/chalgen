FROM python:3.9-slim AS build
ADD . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN apt-get update && \
    apt-get install -yq gcc libev-dev
RUN pip install -r requirements.txt
RUN python manage.py

FROM gcr.io/distroless/python3
COPY --from=build /app /app
# copy libev files
COPY --from=build /usr/lib/x86_64-linux-gnu/libev.so.4 /usr/lib/x86_64-linux-gnu/libev.so.4
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
WORKDIR /app
EXPOSE 5000
ENV PYTHONPATH=/usr/local/lib/python3.9/site-packages
ENTRYPOINT python routes.py