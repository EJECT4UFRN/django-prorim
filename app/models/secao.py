from django.db import models
from app.models.sala import Sala
from app.models.choice_periodo_turno import ChoicePeriodoTurno
from app.strings import (
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_DATA,
    VERBOSE_PERIODO,
    VERBOSE_SALA,
    VERBOSE_SECAO,
    VERBOSE_PLURAL_SECAO,
)


class Secao(models.Model):
    """ Seção, agrupamento de data, período e sala, usado para gestão de
    enfermagem. Ex: 19/07/2017 à tarde na sala 1.  """

    class Meta:
        verbose_name = VERBOSE_SECAO
        verbose_name_plural = VERBOSE_PLURAL_SECAO
        ordering = ['-data']

    criado = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name=VERBOSE_CRIADO,
    )
    atualizado = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        verbose_name=VERBOSE_ATUALIZADO,
    )
    data = models.DateTimeField(
        verbose_name=VERBOSE_DATA,
    )
    periodo = models.ForeignKey(
        ChoicePeriodoTurno,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_PERIODO,
    )
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_SALA,
    )
