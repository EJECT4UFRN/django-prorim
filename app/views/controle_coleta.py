from rest_framework import viewsets
from app.models import ControleColeta
from app.serializers import ControleColetaSerializer


class ControleColetaView(viewsets.ModelViewSet):
    queryset = ControleColeta.objects.all()
    serializer_class = ControleColetaSerializer
    