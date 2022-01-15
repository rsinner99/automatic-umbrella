FROM python:3.10-buster
WORKDIR /code

ARG docker_host

ENV RCA_DB_URL=$docker_host
ENV RCA_CSV_PATH="eval_results.csv"
ENV RCA_REPORT_DIR="eval_reports"


RUN apt-get update
RUN apt-get install -y curl musl-dev gcc libffi-dev chromium-driver
RUN export PATH=/usr/bin/chromedriver:$PATH

COPY ./requirements.txt .
RUN python -m pip install -U pip setuptools
RUN python -m pip install -r ./requirements.txt

COPY . .

ENTRYPOINT python -m unittest discover && TraceExplorer
