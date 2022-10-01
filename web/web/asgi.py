"""
ASGI config for web project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from .tracing import setup_tracing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
SERVICE_NAME = os.environ.get('SERVICE_NAME')

setup_tracing(SERVICE_NAME)
asgi_application = get_asgi_application()


from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from frontend import consumers


application = ProtocolTypeRouter({
    "http": asgi_application,
    "websocket": AuthMiddlewareStack(
        URLRouter(
        [path('tasks/notification_testing/', consumers.NotificationConsumer.as_asgi())]
        ))
})