from django.db import models
from app.strings import (
    VERBOSE_CONVENIO,
    VERBOSE_ANO,
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_CONTROLE_FINANCEIRO,
    VERBOSE_PLURAL_CONTROLE_FINANCEIRO,
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

class ControleFinanceiro(models.Model):
    """ Controle do total de arrecadação de cada convênio por mês.  """

    class Meta:
        verbose_name = VERBOSE_CONTROLE_FINANCEIRO
        verbose_name_plural = VERBOSE_PLURAL_CONTROLE_FINANCEIRO

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
    ano = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_ANO,
    )
    convenio = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_CONVENIO,
    )
    janeiro = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_JANEIRO,
    )
    fevereiro = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_FEVEREIRO,
    )
    marco = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_MARCO,
    )
    abril = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_ABRIL,
    )
    maio = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_MAIO,
    )
    junho = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_JUNHO,
    )
    julho = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_JULHO,
    )
    agosto = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_AGOSTO,
    )
    setembro = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_SETEMBRO,
    )
    outubro = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_OUTRUBRO,
    )
    novembro = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_NOVEMBRO,
    )
    dezembro = models.FloatField(
        blank=True,
        null=True,
        verbose_name=VERBOSE_DEZEMBRO,
    )
