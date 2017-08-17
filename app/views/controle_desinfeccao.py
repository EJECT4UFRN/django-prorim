# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ControleDesinfeccao
from app.serializers import ControleDesinfeccaoSerializer


class ControleDesinfeccaoView(viewsets.ModelViewSet):
    queryset = ControleDesinfeccao.objects.all()
    serializer_class = ControleDesinfeccaoSerializer
    permission_classes = (IsAuthenticated,)
