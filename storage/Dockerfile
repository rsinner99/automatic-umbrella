FROM python:3.8

RUN mkdir /code
WORKDIR /code

COPY ./storage/requirements.txt ./
RUN pip install -r requirements.txt

ADD ./storage/tasks/ ./
ADD ./celery_tasks/ ./

ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n worker.storage.%h --queues=storage,default