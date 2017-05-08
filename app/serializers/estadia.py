from rest_framework import serializers
from app.models import Estadia, Erro

class CleanErroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Erro
        fields = fields = '__all__'
        depth = 1


class EstadiaSerializer(serializers.ModelSerializer):
    erro = CleanErroSerializer()

    class Meta:
        model = Estadia
        fields = fields = '__all__'
        depth = 1
        