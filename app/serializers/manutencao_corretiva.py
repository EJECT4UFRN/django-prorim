from rest_framework import serializers
from app.models import ManutencaoCorretiva


class ManutencaoCorretivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManutencaoCorretiva
        fields = '__all__'
        depth = 4


class ShallowManutencaoCorretivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManutencaoCorretiva
        fields = '__all__'


class NoRelationManutencaoCorretivaSerializer(serializers.ModelSerializer):
    """ Classe sem as relações de chave estrangeiro do model. """

    class Meta:
        model = ManutencaoCorretiva
        exclude = ('erro',)
        depth = 1
