from rest_framework import viewsets
from app.models import ManutencaoPreventiva
from app.serializers import ManutencaoPreventivaSerializer


class ManutencaoPreventivaView(viewsets.ModelViewSet):
    queryset = ManutencaoPreventiva.objects.all()
    serializer_class = ManutencaoPreventivaSerializer
    