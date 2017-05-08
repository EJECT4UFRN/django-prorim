from django.db import models
from django.contrib.auth.models import User
from app.models.sala import Sala
from app.models.maquina import Maquina
from app.strings import (
    VERBOSE_TURNO,
    VERBOSE_PLURAL_TURNO,
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_DATA,
    VERBOSE_PERIODO,
    VERBOSE_SALA,
    VERBOSE_ESTADIA,
    VERBOSE_PLURAL_ESTADIA,
    VERBOSE_NUMERO_DA_MACA,
    VERBOSE_PACIENTE,
    VERBOSE_INICIO,
    VERBOSE_FIM,
    VERBOSE_ERRO,
    VERBOSE_PLURAL_ERRO,
    VERBOSE_NUMERO,
    VERBOSE_OBSERVACAO,
    VERBOSE_OCORRIDO,
    VERBOSE_CONCLUIDO,
    VERBOSE_ENFERMEIRO,
    VERBOSE_MAQUINA,
    VERBOSE_MANUTENCAO_CORRETIVA,
    VERBOSE_PLURAL_MANUTENCAO_CORRETIVA,
    VERBOSE_ACAO,
    VERBOSE_TECNICO,
)

class Turno(models.Model):
    """ Exibido  """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_TURNO
        verbose_name_plural = VERBOSE_PLURAL_TURNO

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
    periodo = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_PERIODO,
    )
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_SALA,
        related_name='turno',
    )

    def get_estadias(self):
        """ Retorna as estadias que ocorreram nesse turno. """
        return Estadia.objects.all().filter(turno=self)


class Estadia(models.Model):
    """ Exibido  """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_ESTADIA
        verbose_name_plural = VERBOSE_PLURAL_ESTADIA

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
    turno = models.ForeignKey(
        Turno,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_TURNO,
        related_name='estadias',
    )
    numero_da_maca = models.IntegerField(
        verbose_name=VERBOSE_NUMERO_DA_MACA,
    )
    paciente = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_PACIENTE,
    )
    inicio = models.DateTimeField(
        verbose_name=VERBOSE_INICIO,
    )
    fim = models.DateTimeField(
        verbose_name=VERBOSE_FIM,
    )

    def get_erro(self):
        """ Retorna o erro que ocorreu nessa estadia ou nulo se não houver
        nenhum """
        erro = Erro.objects.all.filter(estadia=self)
        if erro:
            return erro[0]
        else:
            return None


class Erro(models.Model):
    """ Exibido  """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_ERRO
        verbose_name_plural = VERBOSE_PLURAL_ERRO

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
    observacao = models.TextField(
        verbose_name=VERBOSE_OBSERVACAO,
    )
    ocorrido = models.DateTimeField(
        verbose_name=VERBOSE_OCORRIDO,
    )
    concluido = models.DateTimeField(
        verbose_name=VERBOSE_CONCLUIDO,
    )
    enfermeiro = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_ENFERMEIRO,
    )
    estadia = models.OneToOneField(
        Estadia,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_ESTADIA,
        related_name='erro',
    )
    maquina = models.OneToOneField(
        Maquina,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_MAQUINA,
    )

    def get_manutencao_corretiva(self):
        """ Retorna a manutenção corretiva desse erro, se não houver nenhuma
        retorna nulo. """
        corretiva = ManutencaoCorretiva.objects.all().filter(erro=self)
        if corretiva:
            return corretiva[0]
        else:
            return None

class ManutencaoCorretiva(models.Model):
    """ Exibido  """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = VERBOSE_MANUTENCAO_CORRETIVA
        verbose_name_plural = VERBOSE_PLURAL_MANUTENCAO_CORRETIVA

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
    erro = models.OneToOneField(
        Erro,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_ERRO,
        related_name='manutencao_corretiva',
    )
    acao = models.TextField(
        verbose_name=VERBOSE_ACAO,
    )
    tecnico = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=VERBOSE_TECNICO,
    )
