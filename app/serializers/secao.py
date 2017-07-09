from rest_framework import serializers
from app.models import Secao
from app.serializers.estadia import NoRelationEstadiaSerializer


class SecaoSerializer(serializers.ModelSerializer):
    estadias = NoRelationEstadiaSerializer(many=True)

    class Meta:
        model = Secao
        fields = '__all__'
        depth = 1


class ShallowSecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secao
        fields = '__all__'
