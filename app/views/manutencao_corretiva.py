# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ManutencaoCorretiva
from app.serializers import ManutencaoCorretivaSerializer, ShallowManutencaoCorretivaSerializer


class ManutencaoCorretivaView(viewsets.ModelViewSet):
    queryset = ManutencaoCorretiva.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowManutencaoCorretivaSerializer
        else:
            return ManutencaoCorretivaSerializer
