# -*- coding: utf-8 -*-
from rest_framework import viewsets
from app.models import ChoiceDisponibilidadeMaquina
from app.serializers import ChoiceDisponibilidadeMaquinaSerializer


class ChoiceDisponibilidadeMaquinaView(viewsets.ModelViewSet):
    queryset = ChoiceDisponibilidadeMaquina.objects.all()
    serializer_class = ChoiceDisponibilidadeMaquinaSerializer
