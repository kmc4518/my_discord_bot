FROM python:latest

RUN apt-get update -y

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt