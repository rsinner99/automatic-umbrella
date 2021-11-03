FROM python:3.8

RUN mkdir /code
WORKDIR /code

COPY ./calculator/requirements.txt ./
RUN pip install -r requirements.txt

ADD ./calculator/main.py ./
ADD ./celery_tasks/ ./

ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n worker.calc.%h --queues=calc,default