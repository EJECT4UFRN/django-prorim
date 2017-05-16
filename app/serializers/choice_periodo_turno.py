from rest_framework import serializers
from app.models import ChoicePeriodoTurno

class ChoicePeriodoTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoicePeriodoTurno
        fields = '__all__'
