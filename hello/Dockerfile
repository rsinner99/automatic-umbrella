FROM python:3.8

RUN mkdir /code
WORKDIR /code

ADD ./hello/main.py ./
ADD ./celery_tasks/worker.py ./config.py
COPY ./hello/requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n scripts.hello.%h --queues=hello