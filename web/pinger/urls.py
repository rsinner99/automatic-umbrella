from django.urls import path

from . import views

urlpatterns = [
    path('ping_host', views.PingView.as_view(), name="ping"),
]