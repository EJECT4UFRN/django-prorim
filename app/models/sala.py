from django.db import models
from app.strings import (
    VERBOSE_SALA,
    VERBOSE_PLURAL_SALA,
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_NUMERO_DE_MACAS,
    VERBOSE_IDENTIFICADOR,
)

class Sala(models.Model):
    """ Local onde serão realizadas as estadias.  """

    class Meta:
        verbose_name = VERBOSE_SALA
        verbose_name_plural = VERBOSE_PLURAL_SALA

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
    numero_de_macas = models.IntegerField(
        verbose_name=VERBOSE_NUMERO_DE_MACAS,
    )
    identificador = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_IDENTIFICADOR,
    )

    def __str__(self):
        return str(self.identificador)
