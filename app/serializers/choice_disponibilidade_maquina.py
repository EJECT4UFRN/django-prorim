from rest_framework import serializers
from app.models import ChoiceDisponibilidadeMaquina

class ChoiceDisponibilidadeMaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceDisponibilidadeMaquina
        fields = '__all__'
