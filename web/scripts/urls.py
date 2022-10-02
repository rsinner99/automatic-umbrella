from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'doc', views.DocViewSet, basename='doc')
router.register(r'peer', views.PeerViewSet, basename='peer')

urlpatterns = [
    path('run_script', views.ScriptView.as_view(), name="run"),
]


urlpatterns += router.urls