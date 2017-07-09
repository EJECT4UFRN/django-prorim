from rest_framework import viewsets
from app.models import ChoicePeriodoTurno
from app.serializers import ChoicePeriodoTurnoSerializer


class ChoicePeriodoTurnoView(viewsets.ModelViewSet):
    queryset = ChoicePeriodoTurno.objects.all()
    serializer_class = ChoicePeriodoTurnoSerializer
