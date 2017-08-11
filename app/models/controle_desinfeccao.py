from django.db import models
from app.strings import (
    VERBOSE_CONTROLE_DESINFECCAO,
    VERBOSE_PLURAL_CONTROLE_DESINFECCAO,
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_DATA,
    VERBOSE_MOTIVO,
    VERBOSE_REALIZADO,
    VERBOSE_OBSERVACAO,
)

class ControleDesinfeccao(models.Model):
    """ Controle de desinfecção da clínica. """

    class Meta:
        verbose_name = VERBOSE_CONTROLE_DESINFECCAO
        verbose_name_plural = VERBOSE_PLURAL_CONTROLE_DESINFECCAO
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
    motivo = models.TextField(
        verbose_name=VERBOSE_MOTIVO,
    )
    realizado = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_REALIZADO,
    )
    observacao = models.TextField(
        default='',
        blank=True,
        verbose_name=VERBOSE_OBSERVACAO,
    )
