from django.db import models
from app.strings import (
    VERBOSE_CHOICE_EXAME_COLETA,
    VERBOSE_PLURAL_CHOICE_EXAME_COLETA,
    VERBOSE_NOME,
)

class ChoiceExameColeta(models.Model):
    """ Exibido na view 'Controle de coleta'. """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_CHOICE_EXAME_COLETA
        verbose_name_plural = VERBOSE_PLURAL_CHOICE_EXAME_COLETA

    nome = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_NOME,
    )
