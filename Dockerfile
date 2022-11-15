FROM python:latest

RUN apt-get update -y

RUN pip install discord spotipy
