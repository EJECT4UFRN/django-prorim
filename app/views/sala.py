# -*- coding: utf-8 -*-
from rest_framework import viewsets
from app.models import Sala
from app.serializers import SalaSerializer


class SalaView(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
