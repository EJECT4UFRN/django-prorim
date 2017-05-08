from rest_framework import serializers
from app.models import ControleColeta

class ControleColetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleColeta
        fields = fields = '__all__'
