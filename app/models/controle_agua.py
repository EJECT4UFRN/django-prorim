from django.db import models
from app.strings import (
    VERBOSE_CONTROLE_AGUA,
    VERBOSE_PLURAL_CONTROLE_AGUA,
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_DATA,
    VERBOSE_TESTE,
    VERBOSE_RESULTADO,
)

class ControleAgua(models.Model):
    """ Criado, editado, exibido na view 'Controle água'. """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_CONTROLE_AGUA
        verbose_name_plural = VERBOSE_PLURAL_CONTROLE_AGUA

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
    teste = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_TESTE,
    )
    resultado = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_RESULTADO,
    )
