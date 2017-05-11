from rest_framework import viewsets
from app.models import Maquina
from app.serializers import MaquinaSerializer


class MaquinaView(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
    