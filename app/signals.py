# -*- coding: utf-8 -*-
from django.db import models
from django.dispatch import receiver
from app.models import Erro, ManutencaoCorretiva, Maquina, ManutencaoPreventiva

@receiver(models.signals.post_save, sender=Erro)
def execute_on_erro_save(sender, instance, created, *args, **kwargs):
    if created:
        ManutencaoCorretiva.objects.create(erro=instance)

@receiver(models.signals.post_save, sender=Maquina)
def execute_on_maquina_save(sender, instance, created, *args, **kwargs):
    if created:
        ManutencaoPreventiva.objects.create(maquina=instance)
