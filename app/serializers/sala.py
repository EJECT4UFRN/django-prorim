from rest_framework import serializers
from app.models import Sala

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = fields = '__all__'
