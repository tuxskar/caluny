__author__ = 'tuxskar'
from django.apps import AppConfig


class CalunyAppConfig(AppConfig):

    name = 'caluny'
    verbose_name = 'Calendar university administrator'

    def ready(self):
        import caluny.signals.signals

