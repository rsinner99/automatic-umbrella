# pull official base image
FROM python:3.9.6-alpine

RUN apk update
RUN apk add musl-dev mariadb-dev gcc

# set work directory
RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./web ./

# install dependencies
RUN pip install virtualenv
RUN virtualenv venv
RUN pip install --upgrade pip
RUN source venv/bin/activate
RUN pip install -r requirements.txt
