FROM python:3.8

RUN mkdir /code
WORKDIR /code

ADD ./storage/tasks/ ./
ADD ./celery_tasks/worker.py ./config.py
COPY ./storage/requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n worker.storage.%h --queues=storage