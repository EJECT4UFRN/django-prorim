from rest_framework import viewsets
from app.models import ManutencaoCorretiva
from app.serializers import ManutencaoCorretivaSerializer


class ManutencaoCorretivaView(viewsets.ModelViewSet):
    queryset = ManutencaoCorretiva.objects.all()
    serializer_class = ManutencaoCorretivaSerializer
    