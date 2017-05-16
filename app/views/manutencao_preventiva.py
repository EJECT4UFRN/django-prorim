from rest_framework import viewsets
from app.models import ManutencaoPreventiva
from app.serializers import ManutencaoPreventivaSerializer, PureManutencaoPreventivaSerializer


class ManutencaoPreventivaView(viewsets.ModelViewSet):
    queryset = ManutencaoPreventiva.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return PureManutencaoPreventivaSerializer
        else:
            return ManutencaoPreventivaSerializer
    