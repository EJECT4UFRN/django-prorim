from rest_framework import viewsets
from app.models import ChoiceStatusPaciente
from app.serializers import ChoiceStatusPacienteSerializer


class ChoiceStatusPacienteView(viewsets.ModelViewSet):
    queryset = ChoiceStatusPaciente.objects.all()
    serializer_class = ChoiceStatusPacienteSerializer
