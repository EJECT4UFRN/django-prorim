# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ChoiceDisponibilidadeMaquina
from app.serializers import ChoiceDisponibilidadeMaquinaSerializer


class ChoiceDisponibilidadeMaquinaView(viewsets.ModelViewSet):
    queryset = ChoiceDisponibilidadeMaquina.objects.all()
    serializer_class = ChoiceDisponibilidadeMaquinaSerializer
    permission_classes = (IsAuthenticated,)
