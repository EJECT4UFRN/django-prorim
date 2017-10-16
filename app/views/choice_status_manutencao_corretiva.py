# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ChoiceStatusManutencaoCorretiva
from app.serializers import ChoiceStatusManutencaoCorretivaSerializer


class ChoiceStatusManutencaoCorretivaView(viewsets.ModelViewSet):
    queryset = ChoiceStatusManutencaoCorretiva.objects.all()
    serializer_class = ChoiceStatusManutencaoCorretivaSerializer
    permission_classes = (IsAuthenticated,)
