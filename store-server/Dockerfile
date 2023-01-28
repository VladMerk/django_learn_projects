FROM python:3-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src

ADD requirements.txt requirements.txt

RUN python -m pip install --upgrade pip setuptools
RUN python -m pip install -r requirements.txt

COPY ./src /usr/src/
