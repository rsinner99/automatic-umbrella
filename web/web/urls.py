"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import RedirectView
from django.contrib import admin


urlpatterns = [
    path('frontend/admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('scripts/', include('scripts.urls')),
    path('storage/', include('storage.urls')),
    path('pinger/', include('pinger.urls')),
    path('calc/', include('calculator.urls')),
    path('api/', include('api.urls')),
    path('frontend/', include('frontend.urls')),

    path('', RedirectView.as_view(url='/frontend', permanent=True), name='index')

]
