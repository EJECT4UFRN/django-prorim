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
    VERBOSE_DATA,
    VERBOSE_ANO,
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
    data_janeiro = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_JANEIRO,
        blank=True,
        null=True,
    )
    fevereiro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_FEVEREIRO,
    )
    data_fevereiro = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_FEVEREIRO,
        blank=True,
        null=True,
    )
    marco = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_MARCO,
    )
    data_marco = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_MARCO,
        blank=True,
        null=True,
    )
    abril = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_ABRIL,
    )
    data_abril = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_ABRIL,
        blank=True,
        null=True,
    )
    maio = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_MAIO,
    )
    data_maio = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_MAIO,
        blank=True,
        null=True,
    )
    junho = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_JUNHO,
    )
    data_junho = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_JUNHO,
        blank=True,
        null=True,
    )
    julho = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_JULHO,
    )
    data_julho = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_JULHO,
        blank=True,
        null=True,
    )
    agosto = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_AGOSTO,
    )
    data_agosto = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_AGOSTO,
        blank=True,
        null=True,
    )
    setembro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_SETEMBRO,
    )
    data_setembro = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_SETEMBRO,
        blank=True,
        null=True,
    )
    outubro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_OUTRUBRO,
    )
    data_outubro = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_OUTRUBRO,
        blank=True,
        null=True,
    )
    novembro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_NOVEMBRO,
    )
    data_novembro = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_NOVEMBRO,
        blank=True,
        null=True,
    )
    dezembro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_DEZEMBRO,
    )
    data_dezembro = models.DateTimeField(
        default=None,
        verbose_name=VERBOSE_DATA+' '+VERBOSE_DEZEMBRO,
        blank=True,
        null=True,
    )
