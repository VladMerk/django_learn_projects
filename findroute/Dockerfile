FROM python:3-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD requirements.txt requirements.txt

RUN apk upgrade
RUN python -m pip install --upgrade pip setuptools && python -m pip install -r requirements.txt

COPY ./src /app/
