from django.urls import path

from frontend import consumers

websocket_urlpatterns = [
    path('ws', consumers.NotificationConsumer.as_asgi(), name="ws"),
]