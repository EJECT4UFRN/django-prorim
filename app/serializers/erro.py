from rest_framework import serializers
from app.models import Erro, ManutencaoCorretiva

class CleanManutencaoCorretivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManutencaoCorretiva
        exclude = ('erro',)
        depth = 1


class ErroSerializer(serializers.ModelSerializer):
    manutencao_corretiva = CleanManutencaoCorretivaSerializer()

    class Meta:
        model = Erro
        fields = '__all__'
        depth = 1
