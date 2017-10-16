from rest_framework import serializers
from app.models import Estadia, Secao
from app.serializers.erro import ErroSerializer


class ShallowSecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secao
        fields = '__all__'


class EstadiaSerializer(serializers.ModelSerializer):
    erro = ErroSerializer()

    class Meta:
        model = Estadia
        fields = '__all__'
        depth = 2


class NoRelationEstadiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadia
        fields = '__all__'
        depth = 2


class ShallowEstadiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadia
        fields = '__all__'

    @staticmethod
    def process_secao(data):
        """ Acha a seção correspondente com  as informações da data, periodo
        e sala, se não existir uma seção correspondente, cria uma. """
        if ('sala' in data) and ('data' in data) and ('periodo' in data):
            secao_data = {
                'data': data.pop('data'),
                'periodo': data.pop('periodo'),
                'sala': data.pop('sala')
            }
            secao_serial = ShallowSecaoSerializer(data=secao_data)
            secao_serial.is_valid()
            filtro = secao_serial.validated_data
            query = Secao.objects.all().filter(
                data=filtro['data'],
                periodo=filtro['periodo'],
                sala=filtro['sala']
            )
            if query:
                secao = query[0]
            else:
                secao = secao_serial.save()
            data['secao'] = secao.id

    def to_internal_value(self, data):
        self.process_secao(data)
        validated_data = super(ShallowEstadiaSerializer, self).to_internal_value(data)
        if 'erro_data' in data:
            validated_data['erro_data'] = data.pop('erro_data')
        if 'erro' in data:
            try:
                if 'numero' in data['erro']:
                    validated_data['erro_data'] = data.pop('erro')
            except:
                pass
        return validated_data
