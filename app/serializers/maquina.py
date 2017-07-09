from rest_framework import serializers
from app.models import Maquina
from app.serializers.erro import ErroSerializer


class MaquinaSerializer(serializers.ModelSerializer):
    erros = ErroSerializer(many=True)

    class Meta:
        model = Maquina
        fields = '__all__'
        depth = 1


class ShallowMaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'
