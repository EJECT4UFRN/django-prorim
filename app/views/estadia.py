from rest_framework import viewsets
from app.serializers import EstadiaSerializer, PureEstadiaSerializer
from app.models import Estadia


class EstadiaView(viewsets.ModelViewSet):
    queryset = Estadia.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return PureEstadiaSerializer
        else:
            return EstadiaSerializer
            