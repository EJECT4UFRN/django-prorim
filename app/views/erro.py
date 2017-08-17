# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.serializers import ErroSerializer, ShallowErroSerializer
from app.models import Erro


class ErroView(viewsets.ModelViewSet):
    queryset = Erro.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowErroSerializer
        return ErroSerializer
