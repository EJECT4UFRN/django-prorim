from django.db import models

class TestModel(models.Model):
    """ Test, deletar em produção. """

    class Meta:
        """ Selecionar strings que serão usadas no front 'admin'. """
        verbose_name = "TestModel"
        verbose_name_plural = "TestModels"

    criado = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name="Criado",
    )
    atualizado = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        verbose_name="Atualizado",
    )
    arquivo_resultado = models.FileField(
        verbose_name = "Arquivo",
        upload_to='uploads/%Y/%m/%d/',
        blank=True,
    )
