from rest_framework import serializers
from app.models import ChoicePeriodoTurno

class ChoicePeriodoTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoicePeriodoTurno
        fields = fields = '__all__'
