from django.urls import path

from . import views

urlpatterns = [
    path('file', views.FileView.as_view(), name="file"),
]