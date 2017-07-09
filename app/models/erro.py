from django.db import models
from django.contrib.auth.models import User
from app.models.maquina import Maquina
from app.models.estadia import Estadia
from app.strings import (
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_ESTADIA,
    VERBOSE_ERRO,
    VERBOSE_PLURAL_ERRO,
    VERBOSE_NUMERO,
    VERBOSE_OBSERVACAO,
    VERBOSE_OCORRIDO,
    VERBOSE_CONCLUIDO,
    VERBOSE_ENFERMEIRO,
    VERBOSE_MAQUINA,
)

class Erro(models.Model):
    """ Erro ocorrido em alguma máquina durante alguma estadia.  """

    class Meta:
        verbose_name = VERBOSE_ERRO
        verbose_name_plural = VERBOSE_PLURAL_ERRO
        ordering = ['-ocorrido']

    criado = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name=VERBOSE_CRIADO,
    )
    atualizado = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name=VERBOSE_ATUALIZADO,
    )
    numero = models.IntegerField(
        verbose_name=VERBOSE_NUMERO,
    )
    observacao = models.TextField(
        verbose_name=VERBOSE_OBSERVACAO,
        blank=True,
    )
    ocorrido = models.DateTimeField(
        verbose_name=VERBOSE_OCORRIDO,
    )
    concluido = models.DateTimeField(
        verbose_name=VERBOSE_CONCLUIDO,
        blank=True,
        null=True,
    )
    enfermeiro = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_ENFERMEIRO,
        blank=True,
        null=True,
    )
    estadia = models.OneToOneField(
        Estadia,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_ESTADIA,
        related_name='erro',
        blank=True,
        null=True,
    )
    maquina = models.ForeignKey(
        Maquina,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_MAQUINA,
        related_name='erros',
    )

    def __str__(self):
        return str(self.numero)
