FROM python:3.8

RUN mkdir /code
WORKDIR /code

COPY ./pinger/requirements.txt ./
RUN pip install -r requirements.txt

ADD ./pinger/main.py ./
ADD ./celery_tasks/ ./

ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n worker.pinger.%h --queues=pinger,default