# coding=utf-8
from rest_framework import serializers
from app.models import ControleAgua

class ControleAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleAgua
        fields = '__all__'
        depth = 1

class ShallowControleAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleAgua
        fields = '__all__'

    # def to_internal_value(self, data):
    #     validated_data = {}
    #     if 'arquivoResultado' in data:
    #         validated_data['arquivo_resultado'] = data.get('arquivoResultado')
    #     return validated_data

class FileControleAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleAgua
        fields = '__all__'

    def to_internal_value(self, data):
        validated_data = {}
        if 'arquivoResultado' in data:
            validated_data['arquivo_resultado'] = data.get('arquivoResultado')
        return validated_data
