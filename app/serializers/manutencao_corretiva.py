from rest_framework import serializers
from app.models import ManutencaoCorretiva

class ManutencaoCorretivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManutencaoCorretiva
        fields = '__all__'
        depth = 1
