from rest_framework import viewsets
from app.models import ControleAgua
from app.serializers import ControleAguaSerializer


class ControleAguaView(viewsets.ModelViewSet):
    queryset = ControleAgua.objects.all()
    serializer_class = ControleAguaSerializer
    