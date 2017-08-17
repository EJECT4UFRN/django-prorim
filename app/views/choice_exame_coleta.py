# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ChoiceExameColeta
from app.serializers import ChoiceExameColetaSerializer


class ChoiceExameColetaView(viewsets.ModelViewSet):
    queryset = ChoiceExameColeta.objects.all()
    serializer_class = ChoiceExameColetaSerializer
    permission_classes = (IsAuthenticated,)
