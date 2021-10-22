FROM python:3.8

RUN mkdir /code
WORKDIR /code

ADD ./scripts/tasks/ ./
ADD ./celery_tasks/worker.py ./config.py
COPY ./scripts/requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n worker.scripts.%h --queues=scripts