__author__ = 'tuxskar'
from django.apps import AppConfig


class CalunyAppConfig(AppConfig):

    name = 'core'
    verbose_name = 'Calendar university administrator'

    def ready(self):
        import core.signals.signals
