from rest_framework import serializers
from app.models import ChoiceExameColeta

class ChoiceExameColetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceExameColeta
        fields = fields = '__all__'


