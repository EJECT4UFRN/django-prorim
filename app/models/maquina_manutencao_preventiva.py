from django.db import models
from django.dispatch import receiver
from app.models.choice_disponibilidade_maquina import ChoiceDisponibilidadeMaquina
from app.strings import (
    VERBOSE_MAQUINA,
    VERBOSE_PLURAL_MAQUINA,
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_NUMERO,
    VERBOSE_FABRICANTE,
    VERBOSE_DISPONIBILIDADE,
    VERBOSE_MANUTENCAO_PREVENTIVA,
    VERBOSE_PLURAL_MANUTENCAO_PREVENTIVA,
    VERBOSE_JANEIRO,
    VERBOSE_FEVEREIRO,
    VERBOSE_MARCO,
    VERBOSE_ABRIL,
    VERBOSE_MAIO,
    VERBOSE_JUNHO,
    VERBOSE_JULHO,
    VERBOSE_AGOSTO,
    VERBOSE_SETEMBRO,
    VERBOSE_OUTRUBRO,
    VERBOSE_NOVEMBRO,
    VERBOSE_DEZEMBRO,
)


class Maquina(models.Model):
    """ Exibido  """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_MAQUINA
        verbose_name_plural = VERBOSE_PLURAL_MAQUINA

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
    numero = models.IntegerField(
        verbose_name=VERBOSE_NUMERO,
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

class ManutencaoPreventiva(models.Model):
    """ Exibido  """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_MANUTENCAO_PREVENTIVA
        verbose_name_plural = VERBOSE_PLURAL_MANUTENCAO_PREVENTIVA

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
    maquina = models.ForeignKey(
        Maquina,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_MAQUINA,
    )
    janeiro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_JANEIRO,
    )
    fevereiro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_FEVEREIRO,
    )
    marco = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_MARCO,
    )
    abril = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_ABRIL,
    )
    maio = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_MAIO,
    )
    junho = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_JUNHO,
    )
    julho = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_JULHO,
    )
    agosto = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_AGOSTO,
    )
    setembro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_SETEMBRO,
    )
    outubro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_OUTRUBRO,
    )
    novembro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_NOVEMBRO,
    )
    dezembro = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_DEZEMBRO,
    )

@receiver(models.signals.post_save, sender=Maquina)
def execute_on_maquina_save(sender, instance, created, *args, **kwargs):
    if created:
        ManutencaoPreventiva.objects.create(maquina=instance)
