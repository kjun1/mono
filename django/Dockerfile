FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

RUN mkdir /app
WORKDIR /app

ADD django /app
RUN pip install -r requirements.txt

# CMD python3 manage.py runserver 0.0.0.0:8080