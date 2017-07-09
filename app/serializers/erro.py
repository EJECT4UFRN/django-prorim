from rest_framework import serializers
from app.models import Erro
from app.serializers.manutencao_corretiva import (
    NoRelationManutencaoCorretivaSerializer,
)

class ErroSerializer(serializers.ModelSerializer):
    manutencao_corretiva = NoRelationManutencaoCorretivaSerializer()

    class Meta:
        model = Erro
        fields = '__all__'
        depth = 1


class NoRelationErroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Erro
        exclude = ('estadia',)
        depth = 1


class ShallowErroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Erro
        fields = '__all__'
