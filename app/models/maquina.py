from django.db import models
from app.models.sala import Sala
from app.models.choice_disponibilidade_maquina import ChoiceDisponibilidadeMaquina
from app.strings import (
    VERBOSE_MAQUINA,
    VERBOSE_PLURAL_MAQUINA,
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_NUMERO,
    VERBOSE_FABRICANTE,
    VERBOSE_DISPONIBILIDADE,
    VERBOSE_SALA,
)


class Maquina(models.Model):
    """ Máquina para realizar exames da clínica. """

    class Meta:
        verbose_name = VERBOSE_MAQUINA
        verbose_name_plural = VERBOSE_PLURAL_MAQUINA
        ordering = [
            '-disponibilidade__identificador',
            ]

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
    numero = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_NUMERO,
        unique=True,
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
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_SALA,
    )

    def __str__(self):
        return str(self.numero)
