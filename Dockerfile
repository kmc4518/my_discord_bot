FROM python:latest

ENV SPOTIPY_CLIENT_ID='<your key here>'
ENV SPOTIPY_CLIENT_SECRET='<your key here>'
ENV SPOTIPY_REDIRECT_URI='http://127.0.0.1:9090'
ENV DISCORD_TOKEN='<your key here>'
ENV MASTER_PLAYLIST_TOKEN='<your key here>'
ENV YEAR_PLAYLIST_TOKEN='<your key here>'

RUN apt-get update -y

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["my_discord_bot.py"]