# -*- coding: utf-8 -*-
from django.db import models
from app.strings import (
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_CONTROLE_AGUA,
    VERBOSE_PLURAL_CONTROLE_AGUA,
    VERBOSE_DATA,
    VERBOSE_TESTE,
    VERBOSE_SATISFATORIO,
    VERBOSE_NUMERO_DO_LAUDO,
    VERBOSE_ARQUIVO,
)

class ControleAgua(models.Model):
    """ Controle de água da para a clínica. """

    class Meta:
        verbose_name = VERBOSE_CONTROLE_AGUA
        verbose_name_plural = VERBOSE_PLURAL_CONTROLE_AGUA
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
    teste = models.TextField(
        verbose_name=VERBOSE_TESTE,
    )
    resultado = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_SATISFATORIO,
    )
    numero_do_laudo = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_NUMERO_DO_LAUDO,
    )
    arquivo_resultado = models.FileField(
        verbose_name=VERBOSE_ARQUIVO,
        upload_to='uploads/%Y/%m/%d/',
        blank=True,
    )
