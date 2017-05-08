from django.db import models
from app.strings import (
    VERBOSE_CHOICE_PERIODO_TURNO,
    VERBOSE_PLURAL_CHOICE_PERIODO_TURNO,
    VERBOSE_NOME,
)

class ChoicePeriodoTurno(models.Model):
    """ Exibido na view 'Gestão de enfermagem'. """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_CHOICE_PERIODO_TURNO
        verbose_name_plural = VERBOSE_PLURAL_CHOICE_PERIODO_TURNO

    nome = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_NOME,
    )
