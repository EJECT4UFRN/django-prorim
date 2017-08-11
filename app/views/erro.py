# -*- coding: utf-8 -*-
from rest_framework import viewsets
from app.serializers import ErroSerializer, ShallowErroSerializer
from app.models import Erro


class ErroView(viewsets.ModelViewSet):
    queryset = Erro.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowErroSerializer
        return ErroSerializer
