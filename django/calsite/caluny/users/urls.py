__author__ = 'tuxskar'

from django.conf.urls import patterns, url
from . import views
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^create_user/$', views.create_app_user, name='create_user'),
)