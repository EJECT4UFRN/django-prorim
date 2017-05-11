from rest_framework import viewsets
from app.serializers import TurnoSerializer, PureTurnoSerializer
from app.models import Turno


class TurnoView(viewsets.ModelViewSet):
    queryset = Turno.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return PureTurnoSerializer
        else:
            return TurnoSerializer
            