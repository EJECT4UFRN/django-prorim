from django.db import models
from app.models.choice_status_paciente import ChoiceStatusPaciente
from app.strings import (
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_PACIENTE,
    VERBOSE_PLURAL_PACIENTE,
    VERBOSE_NOME,
    VERBOSE_STATUS,
    VERBOSE_CONVENIO,
)

class Paciente(models.Model):
    """ Paciente da clínica. """

    class Meta:
        verbose_name = VERBOSE_PACIENTE
        verbose_name_plural = VERBOSE_PLURAL_PACIENTE

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
    convenio = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_CONVENIO,
    )
    status = models.ForeignKey(
        ChoiceStatusPaciente,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_STATUS,
    )

    def __str__(self):
        return str(self.nome)
