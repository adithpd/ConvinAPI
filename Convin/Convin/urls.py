"""
URL configuration for Convin project.

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views import debug

urlpatterns = [
    path('', debug.default_urlconf),
    path('admin/', admin.site.urls),
    path('rest/v1/calendar/', include('calendar_api.urls'))
]