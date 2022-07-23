"""
WSGI config for web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .tracing import setup_tracing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
SERVICE_NAME = os.environ.get('SERVICE_NAME')

setup_tracing(SERVICE_NAME)

application = get_wsgi_application()
