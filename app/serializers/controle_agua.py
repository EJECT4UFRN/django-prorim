from rest_framework import serializers
from app.models import ControleAgua

class ControleAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleAgua
        fields = '__all__'
        depth = 1

class PureControleAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleAgua
        fields = '__all__'
        