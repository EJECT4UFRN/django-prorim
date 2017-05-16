from rest_framework import viewsets
from app.models import Maquina
from app.serializers import MaquinaSerializer, PureMaquinaSerializer


class MaquinaView(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return PureMaquinaSerializer
        else:
            return MaquinaSerializer
    