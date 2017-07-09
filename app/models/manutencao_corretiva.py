from django.db import models
from django.contrib.auth.models import User
from app.models.erro import Erro
from app.strings import (
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_DATA,
    VERBOSE_MANUTENCAO_CORRETIVA,
    VERBOSE_PLURAL_MANUTENCAO_CORRETIVA,
    VERBOSE_ACAO,
    VERBOSE_TECNICO,
    VERBOSE_ERRO,
)

class ManutencaoCorretiva(models.Model):
    """ Manutenção para corrigir um erro ocorrido em uma máquina.  """

    class Meta:
        verbose_name = VERBOSE_MANUTENCAO_CORRETIVA
        verbose_name_plural = VERBOSE_PLURAL_MANUTENCAO_CORRETIVA
        ordering = ['-criado']

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
        blank=True,
        null=True,
    )
    erro = models.OneToOneField(
        Erro,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_ERRO,
        related_name='manutencao_corretiva',
    )
    acao = models.TextField(
        verbose_name=VERBOSE_ACAO,
        blank=True,
        null=True,
    )
    tecnico = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_TECNICO,
        blank=True,
        null=True,
    )
