from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, viewsets
from app.serializers import EstadiaSerializer, PureEstadiaSerializer
from app.models import Estadia


class IndexView(TemplateView):
    template_name = 'index.html'


# class ControleAguaListx(generics.DestroyAPIView):
#     queryset = ControleAgua.objects.all()
#     serializer_class = ControleAguaSerializer


class ControleAguaList(viewsets.ModelViewSet):
    queryset = Estadia.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return PureEstadiaSerializer
        else:
            return EstadiaSerializer
