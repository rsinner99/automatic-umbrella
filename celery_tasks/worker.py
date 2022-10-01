import os
import requests

from celery import Celery
from celery.signals import worker_process_init, task_postrun

from tracing import initialize_tracing
import celery_settings

DEBUG = True

SERVICE_NAME = os.environ.get('SERVICE_NAME')
BROKER_URL = celery_settings.BROKER_URL
REDIS_URL = celery_settings.REDIS_URL
API_URL = os.environ.get('API_URL', 'Failed')

app = Celery('tasks', broker=BROKER_URL, backend=REDIS_URL)
app.config_from_object(celery_settings, namespace='CELERY')
app.autodiscover_tasks()


def post_task(task_id, name, state):
    params = {
        "task": task_id,
        "name": name,
        "state": state
    }
    resp = requests.get(API_URL + f'api/task/update', params=params)
    if resp.status_code == 200:
        return True
    else:
        raise Exception(resp.content)


# workaround: celery workers need to create a tracer instance on process initiation, 
# otherwise no spans are reported
@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    initialize_tracing(SERVICE_NAME)

@task_postrun.connect(weak=False)
def store_task_finished(**kwargs):
    # kwargs are [task_id, task, args, kwargs, retval, state]
    task_id = kwargs.get("task_id")
    task_name = kwargs.get("task")
    state = kwargs.get("state")
    post_task(task_id, task_name, state)