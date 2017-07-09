from rest_framework import serializers
from app.models import ControleFinanceiro

class ControleFinanceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleFinanceiro
        fields = '__all__'

    def to_internal_value(self, data):
        if 'filter' in data:
            try:
                data['ano'] = data['filter']['ano']
            except:
                pass
        print(data)
        validated_data = super(ControleFinanceiroSerializer, self).to_internal_value(data)
        return validated_data
