# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from app.serializers import UserSerializer


class EnfermeiroView(viewsets.ModelViewSet):
    queryset = User.objects.all().filter(groups__name__in=['Enfermeiro'])
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
