from dateutil.parser import parse
from rest_framework import viewsets
from app.serializers import (
    EstadiaSerializer,
    PureEstadiaSerializer,
    PureErroSerializer
)
from app.models import Estadia, Erro



class EstadiaView(viewsets.ModelViewSet):
    queryset = Estadia.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return PureEstadiaSerializer
        else:
            return EstadiaSerializer

    def get_queryset(self):
        if self.action == 'list':
            query = Estadia.objects.all()
            filtro = self.request.query_params
            if filtro:
                if 'sala' in filtro:
                    query = query.filter(sala=filtro['sala'])
                if 'data' in filtro:
                    data = parse(filtro['data'])
                    query = query.filter(
                        data__year=data.year,
                        data__month=data.month,
                        data__day=data.day
                        )
                if 'periodo' in filtro:
                    query = query.filter(periodo=filtro['periodo'])
            return query
        else:
            return Estadia.objects.all()

    def perform_create(self, serializer):
        if 'erro' in  serializer.validated_data:
            erro_data = serializer.validated_data.pop('erro', None)
        else:
            erro_data = None
        estadia = serializer.save()
        if erro_data:
            erro_data['estadia'] = estadia.id
            erro_serie = PureErroSerializer(data=erro_data)
            if erro_serie.is_valid():
                print('valid')
                erro_serie.save()

    def perform_update(self, serializer):
        if 'erro' in  serializer.validated_data:
            erro_data = serializer.validated_data.pop('erro', None)
            erro_id = serializer.validated_data.pop('erro_id', None)
        else:
            erro_data = None
        estadia = serializer.save()
        if erro_data:
            erro_data['estadia'] = estadia.id
            if erro_id:
                erro = Erro.objects.get(id=erro_id)
                erro_serie = PureErroSerializer(erro, data=erro_data)
            else:
                erro_serie = PureErroSerializer(data=erro_data)

            if erro_serie.is_valid():
                print('valid')
                erro_serie.save()
