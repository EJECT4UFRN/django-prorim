from rest_framework import serializers
from app.models import TestModel

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'
