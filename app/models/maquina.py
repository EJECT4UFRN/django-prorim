from django.db import models
from app.models.choice_disponibilidade_maquina import ChoiceDisponibilidadeMaquina
from app.strings import (
    VERBOSE_MAQUINA,
    VERBOSE_PLURAL_MAQUINA,
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_NUMERO,
    VERBOSE_FABRICANTE,
    VERBOSE_DISPONIBILIDADE,
)

class Maquina(models.Model):
    """ Exibido  """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_MAQUINA
        verbose_name_plural = VERBOSE_PLURAL_MAQUINA

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
    fabricante = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_FABRICANTE,
    )
    disponibilidade = models.ForeignKey(
        ChoiceDisponibilidadeMaquina,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_DISPONIBILIDADE,
    )
    