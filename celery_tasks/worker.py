import os
from opentracing_instrumentation.client_hooks import celery as celery_hooks
from opentracing_instrumentation.client_hooks import requests as requests_hooks
from celery import Celery
from celery.signals import worker_process_init, worker_process_shutdown

from tracing import initialize_tracing, close_tracing
import celery_settings

DEBUG = True

BROKER_URL = celery_settings.BROKER_URL
REDIS_URL = celery_settings.REDIS_URL

app = Celery('tasks', broker=BROKER_URL, backend=REDIS_URL)
app.config_from_object(celery_settings, namespace='CELERY')
app.autodiscover_tasks()

celery_hooks.install_patches()
requests_hooks.install_patches()


# workaround: celery workers need to create a tracer instance on process initiation, 
# otherwise no spans are reported
@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    initialize_tracing()

@worker_process_shutdown.connect(weak=False)
def close_celery_tracing(*args, **kwargs):
    close_tracing
