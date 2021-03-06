# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ChoiceTesteAgua
from app.serializers import ChoiceTesteAguaSerializer


class ChoiceTesteAguaView(viewsets.ModelViewSet):
    queryset = ChoiceTesteAgua.objects.all()
    serializer_class = ChoiceTesteAguaSerializer
    permission_classes = (IsAuthenticated,)
