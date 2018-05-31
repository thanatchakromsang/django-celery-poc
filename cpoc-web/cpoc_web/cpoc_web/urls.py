from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

from cpoc_web.views.controller_view import ControllerTemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^controller/', ControllerTemplateView.as_view()),
]
