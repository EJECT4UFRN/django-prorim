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

class PureErroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Erro
        fields = '__all__'

class PureEstadiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadia
        fields = '__all__'

    def to_internal_value(self, data):
        validated_data = super(PureEstadiaSerializer, self).to_internal_value(data)
        if 'erro_id' in data:
            validated_data['erro_id'] = data['erro_id']
        if 'erro' in data:
            validated_data['erro'] = data['erro']
        return validated_data
