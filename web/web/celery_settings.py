import os

#CELERY_RESULT_SERIALIZER = 'json'
#CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_EXTENDED = True
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_ROUTES =  {
    'pinger.*': {'queue': 'pinger'},
    'scripts.*': {'queue': 'scripts'},
    'hello.*': {'queue': 'hello'},
    'storage.*': {'queue': 'storage'},
    'calc.*': {'queue': 'calc'},
    'monitor.*': {'queue': 'monitor'}
}

BROKER_URL = os.environ.get("BROKER_URL", "amqp://guest:guest@localhost//")
REDIS_BASE_URL = os.environ.get("REDIS_URL", "redis://localhost")
REDIS_URL = f"redis://{REDIS_BASE_URL}"