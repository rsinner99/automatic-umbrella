import os

from celery import Celery

BROKER_URL = os.environ.get("BROKER_URL", "amqp://guest:guest@localhost//")
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost")

app = Celery('tasks', broker=BROKER_URL, backend=REDIS_URL)
