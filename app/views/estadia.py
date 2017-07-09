from dateutil.parser import parse
from rest_framework import viewsets
from app.serializers import (
    EstadiaSerializer,
    ShallowEstadiaSerializer,
    ShallowErroSerializer
)
from app.models import Estadia, Erro


class EstadiaView(viewsets.ModelViewSet):
    queryset = Estadia.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowEstadiaSerializer
        return EstadiaSerializer

    def get_queryset(self):
        if self.action == 'list':
            query = Estadia.objects.all()
            filtro = self.request.query_params
            if filtro:
                if 'sala' in filtro:
                    query = query.filter(secao__sala=filtro['sala'])
                    if 'data' in filtro:
                        data = parse(filtro['data'])
                        query = query.filter(
                            secao__data__year=data.year,
                            secao__data__month=data.month,
                            secao__data__day=data.day
                            )
                        if 'periodo' in filtro:
                            query = query.filter(
                                secao__periodo=filtro['periodo']
                                )
                            return query
                if 'paciente' in filtro:
                    return query.filter(paciente=filtro['paciente'])
            return None
        return Estadia.objects.all()

    def perform_create(self, serializer):
        if 'erro' in  serializer.validated_data:
            erro_data = serializer.validated_data.pop('erro', None)
        else:
            erro_data = None
        estadia = serializer.save()
        if erro_data:
            erro_data['estadia'] = estadia.id
            erro_serie = ShallowErroSerializer(data=erro_data)
            if erro_serie.is_valid():
                erro_serie.save()

    def perform_update(self, serializer):
        if 'erro_data' in  serializer.validated_data:
            erro_data = serializer.validated_data.pop('erro_data', None)
            try:
                erro_data['maquina'] = erro_data['maquina']['id']
                erro_data['enfermeiro'] = erro_data['enfermeiro']['id']
            except:
                pass
        else:
            erro_data = None
        estadia = serializer.save()
        if erro_data:
            erro_data['estadia'] = estadia.id
            if 'id' in erro_data:
                erro = Erro.objects.get(id=erro_data['id'])
                erro_serie = ShallowErroSerializer(erro, data=erro_data)
            else:
                erro_serie = ShallowErroSerializer(data=erro_data)
            if erro_serie.is_valid():
                erro_serie.save()
