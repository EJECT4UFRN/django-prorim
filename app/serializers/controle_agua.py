from rest_framework import serializers
from app.models import ControleAgua

class ControleAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleAgua
        fields = fields = '__all__'
