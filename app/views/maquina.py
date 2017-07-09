from rest_framework import viewsets
from app.models import Maquina
from app.serializers import MaquinaSerializer, ShallowMaquinaSerializer


class MaquinaView(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowMaquinaSerializer
        return MaquinaSerializer

    def get_queryset(self):
        if self.action == 'list':
            query = Maquina.objects.all()
            filtro = self.request.query_params
            if filtro:
                if 'sala' in filtro:
                    return query.filter(sala=filtro['sala'])
        return Maquina.objects.all()
