from rest_framework.routers import DefaultRouter

__author__ = 'tuxskar'

from django.conf.urls import url, include

from views import create_app_user, ObtainUserAuthToken, UserGCMRegistration, SubjectSubscribed

router = DefaultRouter()
router.register(r'subject_subscribed', SubjectSubscribed)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^create_user/$', create_app_user, name='create_user'),
    url(r'^register_gcm_user/$', UserGCMRegistration.as_view(), name='register_gcm_user'),
    url(r'^api-token-auth/$', ObtainUserAuthToken.as_view(), name='obtain_token')
]
