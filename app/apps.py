# -*- coding: utf-8 -*-
from django.apps import AppConfig
from app.strings import VERBOSE_APP_NAME


class CustomAppConfig(AppConfig):
    name = 'app'
    verbose_name = VERBOSE_APP_NAME

    def ready(self):
        import app.signals
