from rest_framework import serializers
from app.models import ChoiceStatusManutencaoCorretiva

class ChoiceStatusManutencaoCorretivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceStatusManutencaoCorretiva
        fields = '__all__'
