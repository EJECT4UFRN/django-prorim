# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ChoiceStatusEstadia
from app.serializers import ChoiceStatusEstadiaSerializer


class ChoiceStatusEstadiaView(viewsets.ModelViewSet):
    queryset = ChoiceStatusEstadia.objects.all()
    serializer_class = ChoiceStatusEstadiaSerializer
    permission_classes = (IsAuthenticated,)
