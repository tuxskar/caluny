from caluny_api.chat_messages.models import MessageToSubject
from django.forms import ModelForm


class TeacherMessageForm(ModelForm):
    class Meta:
        model = MessageToSubject
        exclude = ['sender']