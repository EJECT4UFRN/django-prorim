# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ControleColeta
from app.serializers import ShallowControleColetaSerializer, ControleColetaSerializer


class ControleColetaView(viewsets.ModelViewSet):
    queryset = ControleColeta.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowControleColetaSerializer
        else:
            return ControleColetaSerializer
