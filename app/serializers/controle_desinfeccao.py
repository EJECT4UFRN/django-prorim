from rest_framework import serializers
from app.models import ControleDesinfeccao

class ControleDesinfeccaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleDesinfeccao
        fields = fields = '__all__'
