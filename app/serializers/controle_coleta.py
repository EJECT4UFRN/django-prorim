from rest_framework import serializers
from app.models import ControleColeta

class ShallowControleColetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleColeta
        fields = '__all__'


class ControleColetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleColeta
        fields = '__all__'
        depth = 1
