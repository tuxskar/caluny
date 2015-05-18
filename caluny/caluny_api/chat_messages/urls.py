from django.conf.urls import url

from caluny_api.chat_messages import views

urlpatterns = [
    url(r'^send_subject_message/$', views.SendMessageToSubject.as_view(), name='send_subject_message'),
]
