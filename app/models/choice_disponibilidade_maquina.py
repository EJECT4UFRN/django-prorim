from django.db import models
from app.strings import (
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_CHOICE_DISPONIBILIDADE_MAQUINA,
    VERBOSE_PLURAL_CHOICE_DISPONIBILIDADE_MAQUINA,
    VERBOSE_NOME,
    VERBOSE_DESATIVADO,
    VERBOSE_IDENTIFICADOR,
)


class ChoiceDisponibilidadeMaquina(models.Model):
    """ Opções de disponibilidade para maquina.
    Ex: Disponível, Não disponivel, Desativada. """

    class Meta:
        verbose_name = VERBOSE_CHOICE_DISPONIBILIDADE_MAQUINA
        verbose_name_plural = VERBOSE_PLURAL_CHOICE_DISPONIBILIDADE_MAQUINA

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
    nome = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_NOME,
    )
    identificador = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_IDENTIFICADOR,
    )
    desativado = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_DESATIVADO,
    )

    def __str__(self):
        return str(self.nome)
