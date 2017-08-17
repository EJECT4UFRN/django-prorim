# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ChoicePeriodoTurno
from app.serializers import ChoicePeriodoTurnoSerializer


class ChoicePeriodoTurnoView(viewsets.ModelViewSet):
    queryset = ChoicePeriodoTurno.objects.all()
    serializer_class = ChoicePeriodoTurnoSerializer
    permission_classes = (IsAuthenticated,)
