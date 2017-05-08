from rest_framework import serializers
from app.models import Maquina

class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = fields = '__all__'
