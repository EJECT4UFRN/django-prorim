from rest_framework import viewsets
from app.models import ControleAgua
from app.serializers import ControleAguaSerializer, PureControleAguaSerializer


class ControleAguaView(viewsets.ModelViewSet):
    queryset = ControleAgua.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return PureControleAguaSerializer
        else:
            return ControleAguaSerializer
    