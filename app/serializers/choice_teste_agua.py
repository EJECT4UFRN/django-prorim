from rest_framework import serializers
from app.models import ChoiceTesteAgua

class ChoiceTesteAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceTesteAgua
        fields = '__all__'
