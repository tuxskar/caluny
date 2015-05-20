from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from caluny_api.chat_messages import views

router = DefaultRouter()
router.register(r'messages', views.MessagesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^send_subject_message/$', views.SendMessageToSubject.as_view(), name='send_subject_message'),
]
