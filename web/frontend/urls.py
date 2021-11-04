from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('docs/', views.docs, name='docs'),
    path('docs/<int:doc_id>', views.doc_view, name='doc_view'),
    path('docs/create/', views.doc_create, name='doc_create'),

    path('peers/', views.peers, name='peers'),
    path('peers/<int:peer_id>', views.peer_view, name='peer_view'),
    path('peers/create/', views.peer_create, name='peer_create'),

    path('files/', views.files, name='files'),
    path('files/create/', views.create_file, name='file_create'),
    path('files/list', views.list_files, name='file_list'),
    path('files/view/<str:filename>', views.view_file, name='file_view'),

    path('tasks/', views.prepare_task, name="tasks"),
    path('tasks/<str:task_id>', views.show_task_result, name="show_task"),
]
