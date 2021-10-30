FROM python:3.8

RUN mkdir /code
WORKDIR /code

COPY ./scripts/requirements.txt ./
RUN pip install -r requirements.txt

ADD ./scripts/tasks/ ./
ADD ./celery_tasks/ ./

ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n worker.scripts.%h --queues=scripts,default