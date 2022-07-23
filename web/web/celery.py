import os
from celery import Celery
from . import celery_settings
from django.conf import settings
from django.apps import apps

from opentelemetry.instrumentation.celery import CeleryInstrumentor

BROKER_URL = celery_settings.BROKER_URL
REDIS_URL = celery_settings.REDIS_URL

CeleryInstrumentor().instrument()
#app = CeleryTracing('tasks', tracer=DEFAULT_TRACER, propagate=True, broker=BROKER_URL, backend=REDIS_URL)
app = Celery('tasks', broker=BROKER_URL, backend=REDIS_URL)
app.config_from_object(celery_settings, namespace='CELERY')

app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])