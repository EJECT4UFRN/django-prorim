from rest_framework import serializers
from app.models import ChoiceStatusEstadia

class ChoiceStatusEstadiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceStatusEstadia
        fields = '__all__'
