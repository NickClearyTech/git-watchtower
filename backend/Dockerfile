FROM python:3.11-slim-buster

RUN apt-get update && apt-get upgrade -y && apt-get install git -y

WORKDIR /watchtower

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# create an unprivledged user
RUN adduser --disabled-password --gecos '' app

COPY ./requirements.txt .
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

COPY . /watchtower

WORKDIR /watchtower