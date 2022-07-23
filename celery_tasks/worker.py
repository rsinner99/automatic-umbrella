import os

from celery import Celery
from celery.signals import worker_process_init

from tracing import initialize_tracing
import celery_settings

DEBUG = True

SERVICE_NAME = os.environ.get('SERVICE_NAME')
BROKER_URL = celery_settings.BROKER_URL
REDIS_URL = celery_settings.REDIS_URL

app = Celery('tasks', broker=BROKER_URL, backend=REDIS_URL)
app.config_from_object(celery_settings, namespace='CELERY')
app.autodiscover_tasks()


# workaround: celery workers need to create a tracer instance on process initiation, 
# otherwise no spans are reported
@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    initialize_tracing(SERVICE_NAME)
