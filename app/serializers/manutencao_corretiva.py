from rest_framework import serializers
from app.models import ManutencaoCorretiva

class ManutencaoCorretivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManutencaoCorretiva
        fields = '__all__'
        depth = 4

class PureManutencaoCorretivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManutencaoCorretiva
        fields = '__all__'
        