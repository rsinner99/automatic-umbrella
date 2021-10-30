import os

from celery import Celery

import celery_settings

BROKER_URL = celery_settings.BROKER_URL
REDIS_URL = celery_settings.REDIS_URL

app = Celery('tasks', broker=BROKER_URL, backend=REDIS_URL)
app.config_from_object(celery_settings, namespace='CELERY')
app.autodiscover_tasks()
