FROM python:3.8

RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y graphviz

COPY ./monitor/requirements.txt ./
RUN pip install -r requirements.txt

RUN mkdir ./network_graph
RUN git clone https://github.com/LeoVerto/docker-network-graph.git ./network_graph
RUN mv ./network_graph/docker-net-graph.py ./network_graph/run.py

ADD ./monitor/main.py ./
ADD ./celery_tasks/ ./

ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n worker.monitor.%h --queues=monitor,default