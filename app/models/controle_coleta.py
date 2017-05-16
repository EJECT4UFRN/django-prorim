from django.db import models
from app.models.choice_exame_coleta import ChoiceExameColeta
from app.strings import (
    VERBOSE_CONTROLE_COLETA,
    VERBOSE_PLURAL_CONTROLE_COLETA,
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_DATA_REALIZADO,
    VERBOSE_DATA_ENVIO,
    VERBOSE_DATA_RESULTADO,
    VERBOSE_EXAME,
    VERBOSE_RESULTADO,
    VERBOSE_NUMERO_DO_LAUDO,
    VERBOSE_REALIZADO,
)

class ControleColeta(models.Model):
    """ Exibido  """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_CONTROLE_COLETA
        verbose_name_plural = VERBOSE_PLURAL_CONTROLE_COLETA

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
    data_realizado = models.DateTimeField(
        verbose_name=VERBOSE_DATA_REALIZADO,
    )
    data_envio = models.DateTimeField(
        verbose_name=VERBOSE_DATA_ENVIO,
    )
    data_resultado = models.DateTimeField(
        verbose_name=VERBOSE_DATA_RESULTADO,
    )
    exame = models.ForeignKey(
        ChoiceExameColeta,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_EXAME,
    )
    resultado = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_RESULTADO,
    )
    numero_do_laudo = models.IntegerField(
        verbose_name=VERBOSE_NUMERO_DO_LAUDO,
    )
    realizado = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_REALIZADO,
    )
