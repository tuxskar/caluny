from django.contrib import admin

from caluny_api.chat_messages.models import MessageToSubject


@admin.register(MessageToSubject)
class MessageToSubjectAdmin(admin.ModelAdmin):
    pass
