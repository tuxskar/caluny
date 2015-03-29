__author__ = 'tuxskar'
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from core.models import Teacher, Student

@receiver(post_save, sender=Student)
@receiver(post_save, sender=Teacher)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


