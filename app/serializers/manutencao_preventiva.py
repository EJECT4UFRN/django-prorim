from rest_framework import serializers
from app.models import ManutencaoPreventiva

class ManutencaoPreventivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManutencaoPreventiva
        fields = '__all__'
        depth = 1

class PureManutencaoPreventivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManutencaoPreventiva
        fields = '__all__'