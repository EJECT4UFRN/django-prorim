from rest_framework import serializers
from app.models import Erro, ManutencaoCorretiva

class ManutencaoCorretivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManutencaoCorretiva
        fields = fields = '__all__'
        depth = 1


class ErroSerializer(serializers.ModelSerializer):
    manutencao_corretiva = ManutencaoCorretivaSerializer()

    class Meta:
        model = Erro
        fields = fields = '__all__'
        depth = 1
