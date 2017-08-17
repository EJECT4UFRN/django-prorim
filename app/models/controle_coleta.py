from django.db import models
from app.models.choice_exame_coleta import ChoiceExameColeta
from app.models.choice_teste_agua import ChoiceTesteAgua
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
    VERBOSE_OBSERVACAO,
)

class ControleColeta(models.Model):
    """ Controle de controle de coleta da clínica.  """

    class Meta:
        verbose_name = VERBOSE_CONTROLE_COLETA
        verbose_name_plural = VERBOSE_PLURAL_CONTROLE_COLETA
        ordering = ['-data_realizado']

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
        blank=True,
        null=True,
    )
    data_envio = models.DateTimeField(
        verbose_name=VERBOSE_DATA_ENVIO,
        blank=True,
        null=True,
    )
    data_resultado = models.DateTimeField(
        verbose_name=VERBOSE_DATA_RESULTADO,
        blank=True,
        null=True,
    )
    exame = models.ForeignKey(
        ChoiceExameColeta,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_EXAME,
    )
    resultado = models.ForeignKey(
        ChoiceTesteAgua,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_RESULTADO,
        blank=True,
        null=True,
    )
    numero_do_laudo = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_NUMERO_DO_LAUDO,
    )
    realizado = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_REALIZADO,
    )
    observacao = models.TextField(
        default='',
        blank=True,
        verbose_name=VERBOSE_OBSERVACAO,
    )
