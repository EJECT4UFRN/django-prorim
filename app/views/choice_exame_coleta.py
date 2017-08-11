# -*- coding: utf-8 -*-
from rest_framework import viewsets
from app.models import ChoiceExameColeta
from app.serializers import ChoiceExameColetaSerializer


class ChoiceExameColetaView(viewsets.ModelViewSet):
    queryset = ChoiceExameColeta.objects.all()
    serializer_class = ChoiceExameColetaSerializer
