# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import Paciente
from app.serializers import PacienteSerializer, ShallowPacienteSerializer


class PacienteView(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowPacienteSerializer
        return PacienteSerializer

    def get_queryset(self):
        if self.action == 'list':
            query = Paciente.objects.all()
            filtro = self.request.query_params
            if filtro:
                if 'searchNome' in filtro:
                    search_nome = filtro['searchNome']
                    if search_nome:
                        return query.filter(nome__icontains=search_nome)
            return None
        return Paciente.objects.all()
