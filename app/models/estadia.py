from django.db import models
from app.models.secao import Secao
from app.models.paciente import Paciente
from app.models.choice_status_estadia import ChoiceStatusEstadia
from django.core.exceptions import ValidationError
from app.strings import (
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_SECAO,
    VERBOSE_ESTADIA,
    VERBOSE_PLURAL_ESTADIA,
    VERBOSE_NUMERO_DA_MACA,
    VERBOSE_PACIENTE,
    VERBOSE_INICIO,
    VERBOSE_FIM,
    VERBOSE_STATUS
)


class Estadia(models.Model):
    """ Periodo de tempo em que um paciente é atendido em uma sala. """

    class Meta:
        verbose_name = VERBOSE_ESTADIA
        verbose_name_plural = VERBOSE_PLURAL_ESTADIA
        ordering = ['-secao__data', '-inicio']

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
    secao = models.ForeignKey(
        Secao,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_SECAO,
        related_name='estadias',
    )
    numero_da_maca = models.CharField(
        verbose_name=VERBOSE_NUMERO_DA_MACA,
        max_length=150,
        blank=True,
        null=True,
    )
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_PACIENTE,
    )
    inicio = models.DateTimeField(
        verbose_name=VERBOSE_INICIO,
        blank=True,
        null=True,
    )
    fim = models.DateTimeField(
        verbose_name=VERBOSE_FIM,
        blank=True,
        null=True,
    )
    status = models.ForeignKey(
        ChoiceStatusEstadia,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_STATUS,
        blank=True,
        null=True,
    )
