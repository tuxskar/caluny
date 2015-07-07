from django.conf import settings
from model_utils import Choices
from model_utils.models import StatusModel, TimeStampedModel
from django.db import models

from core.models import TeachingSubject


class Message(TimeStampedModel, StatusModel):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()

    STATUS = Choices('TO_SENT', 'SENT')

    class Meta:
        ordering = ('-created', '-modified')


class MessageToSubject(Message):
    receiver = models.ForeignKey(TeachingSubject, db_column='t_subject_id')
