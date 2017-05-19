from rest_framework import serializers
from app.models import Estadia, Erro

class CleanErroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Erro
        exclude = ('estadia',)
        depth = 1


class EstadiaSerializer(serializers.ModelSerializer):
    erro = CleanErroSerializer()

    class Meta:
        model = Estadia
        fields = '__all__'
        depth = 2


class PureEstadiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadia
        fields = '__all__'
