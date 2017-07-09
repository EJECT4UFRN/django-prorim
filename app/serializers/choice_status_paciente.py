from rest_framework import serializers
from app.models import ChoiceStatusPaciente

class ChoiceStatusPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceStatusPaciente
        fields = '__all__'
