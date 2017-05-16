from django.db import models
from app.strings import (
    VERBOSE_CHOICE_TESTE_AGUA,
    VERBOSE_PLURAL_CHOICE_TESTE_AGUA,
    VERBOSE_NOME,
    VERBOSE_DESATIVADO,
)

class ChoiceTesteAgua(models.Model):
    """ Exibido na view 'Coleta de água'. """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_CHOICE_TESTE_AGUA
        verbose_name_plural = VERBOSE_PLURAL_CHOICE_TESTE_AGUA

    nome = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_NOME,
    )
    desativado = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_DESATIVADO,
    )

    def __str__(self):
        return str(self.nome)
