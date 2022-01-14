# pull official base image
FROM python:3.9.6-buster

RUN apt-get update
RUN apt-get install -y musl-dev libmariadb-dev gcc

# set work directory
RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./ ./
