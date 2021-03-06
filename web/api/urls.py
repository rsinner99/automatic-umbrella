from rest_framework_simplejwt import views as simplejwt
from django.urls import path

from . import views

urlpatterns = [
    path('token/', simplejwt.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', simplejwt.TokenRefreshView.as_view(), name='token_refresh'),

    path('task/result', views.ApiTaskView.as_view(), name='api-task-result'),
    path('task/generic_run', views.run_task, name="run_task"),
    path('task/run_and_store', views.ApiScriptStoreView.as_view(), name='api-task-run'),
    path('script/run', views.ApiScriptView.as_view(), name='api-script-run'),
    path('files', views.ApiFileView.as_view(), name='api-files'),
]
