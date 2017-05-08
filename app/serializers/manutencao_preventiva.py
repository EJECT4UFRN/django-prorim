from rest_framework import serializers
from app.models import ManutencaoPreventiva

class ManutencaoPreventivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManutencaoPreventiva
        fields = fields = '__all__'
        depth = 1
