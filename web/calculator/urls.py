from django.urls import path

from . import views

urlpatterns = [
    path('estimate_pi', views.CalcView.as_view(), name="estimate_pi"),
]