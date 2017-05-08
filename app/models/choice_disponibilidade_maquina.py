from django.db import models
from app.strings import (
    VERBOSE_CHOICE_DISPONIBILIDADE_MAQUINA,
    VERBOSE_PLURAL_CHOICE_DISPONIBILIDADE_MAQUINA,
    VERBOSE_NOME,
)

class ChoiceDisponibilidadeMaquina(models.Model):
    """ Exibido na view 'Máquina'. """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_CHOICE_DISPONIBILIDADE_MAQUINA
        verbose_name_plural = VERBOSE_PLURAL_CHOICE_DISPONIBILIDADE_MAQUINA

    nome = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_NOME,
    )
