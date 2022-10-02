from django.urls import path

from . import views

urlpatterns = [
    path('say_hello', views.HelloView.as_view(), name="hello"),
]