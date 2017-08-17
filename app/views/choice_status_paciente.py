# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ChoiceStatusPaciente
from app.serializers import ChoiceStatusPacienteSerializer


class ChoiceStatusPacienteView(viewsets.ModelViewSet):
    queryset = ChoiceStatusPaciente.objects.all()
    serializer_class = ChoiceStatusPacienteSerializer
    permission_classes = (IsAuthenticated,)
