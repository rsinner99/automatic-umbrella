import os
from opentracing_instrumentation.client_hooks import celery as celery_hooks
from opentracing_instrumentation.client_hooks import requests as requests_hooks
from celery_opentracing import CeleryTracing

from tracing import get_tracer
import celery_settings

BROKER_URL = celery_settings.BROKER_URL
REDIS_URL = celery_settings.REDIS_URL
SERVICE_NAME = os.environ.get('SERVICE_NAME')

opentracing_tracer = get_tracer(SERVICE_NAME)
celery_hooks.install_patches()
requests_hooks.install_patches()

#app = CeleryTracing('tasks', tracer=opentracing_tracer, propagate=True, broker=BROKER_URL, backend=REDIS_URL)
from celery import Celery
app = Celery('tasks', broker=BROKER_URL, backend=REDIS_URL)
app.config_from_object(celery_settings, namespace='CELERY')
app.autodiscover_tasks()
