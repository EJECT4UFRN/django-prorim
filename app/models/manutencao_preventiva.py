from django.db import models
from app.models.maquina import Maquina
from app.strings import (
    VERBOSE_MAQUINA,
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_MANUTENCAO_PREVENTIVA,
    VERBOSE_PLURAL_MANUTENCAO_PREVENTIVA,
    VERBOSE_JANEIRO,
    VERBOSE_FEVEREIRO,
    VERBOSE_MARCO,
    VERBOSE_ABRIL,
    VERBOSE_MAIO,
    VERBOSE_JUNHO,
    VERBOSE_JULHO,
    VERBOSE_AGOSTO,
    VERBOSE_SETEMBRO,
    VERBOSE_OUTRUBRO,
    VERBOSE_NOVEMBRO,
    VERBOSE_DEZEMBRO,
)

class ManutencaoPreventiva(models.Model):
    """ Agendamento de manutenções preventivas para uma máquina por mês.  """

    class Meta:
        verbose_name = VERBOSE_MANUTENCAO_PREVENTIVA
        verbose_name_plural = VERBOSE_PLURAL_MANUTENCAO_PREVENTIVA

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
    maquina = models.ForeignKey(
        Maquina,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_MAQUINA,
    )
    janeiro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_JANEIRO,
    )
    fevereiro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_FEVEREIRO,
    )
    marco = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_MARCO,
    )
    abril = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_ABRIL,
    )
    maio = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_MAIO,
    )
    junho = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_JUNHO,
    )
    julho = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_JULHO,
    )
    agosto = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_AGOSTO,
    )
    setembro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_SETEMBRO,
    )
    outubro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_OUTRUBRO,
    )
    novembro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_NOVEMBRO,
    )
    dezembro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_DEZEMBRO,
    )
