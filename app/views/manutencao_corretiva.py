from rest_framework import viewsets
from app.models import ManutencaoCorretiva
from app.serializers import ManutencaoCorretivaSerializer, PureManutencaoCorretivaSerializer


class ManutencaoCorretivaView(viewsets.ModelViewSet):
    queryset = ManutencaoCorretiva.objects.all()
    serializer_class = ManutencaoCorretivaSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return PureManutencaoCorretivaSerializer
        else:
            return ManutencaoCorretivaSerializer
    