import os

#CELERY_RESULT_SERIALIZER = 'json'
#CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_EXTENDED = True
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_ROUTES =  {
    'scripts.*': {'queue': 'scripts'},
    'hello.*': {'queue': 'hello'},
    'storage.*': {'queue': 'storage'},
    'common.*': {'queue': 'default'}
}

BROKER_URL = os.environ.get("BROKER_URL", "amqp://guest:guest@localhost//")
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost")
