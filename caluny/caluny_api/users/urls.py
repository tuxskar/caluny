__author__ = 'tuxskar'

from django.conf.urls import url

from views import create_app_user, ObtainUserAuthToken


urlpatterns = [
    url(r'^create_user/$', create_app_user, name='create_user'),
    url(r'^api-token-auth/$', ObtainUserAuthToken.as_view(), name='obtain_token'),
]