__author__ = 'tuxskar'

from django.conf.urls import patterns, url
from caluny.caluny_api.users import views


urlpatterns = patterns('',
                       url(r'^create_user/$', views.create_app_user, name='create_user'),
                       )