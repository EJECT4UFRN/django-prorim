# -*- coding: utf-8 -*-
from rest_framework import viewsets
from app.models import ManutencaoPreventiva
from app.serializers import ManutencaoPreventivaSerializer, ShallowManutencaoPreventivaSerializer


class ManutencaoPreventivaView(viewsets.ModelViewSet):
    queryset = ManutencaoPreventiva.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowManutencaoPreventivaSerializer
        else:
            return ManutencaoPreventivaSerializer
