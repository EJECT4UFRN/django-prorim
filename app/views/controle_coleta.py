from rest_framework import viewsets
from app.models import ControleColeta
from app.serializers import ShallowControleColetaSerializer, ControleColetaSerializer


class ControleColetaView(viewsets.ModelViewSet):
    queryset = ControleColeta.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowControleColetaSerializer
        else:
            return ControleColetaSerializer
