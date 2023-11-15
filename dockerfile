FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc

WORKDIR /code

RUN pip install --upgrade pip
COPY /requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8089

# ENTRYPOINT ["locust"]