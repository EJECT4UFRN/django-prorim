# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ControleFinanceiro
from app.serializers import ControleFinanceiroSerializer


class ControleFinanceiroView(viewsets.ModelViewSet):
    queryset = ControleFinanceiro.objects.all()
    serializer_class = ControleFinanceiroSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.action == 'list':
            query = ControleFinanceiro.objects.all()
            filtro = self.request.query_params
            if filtro:
                if 'ano' in filtro:
                    return query.filter(ano=filtro['ano'])
            return None
        return ControleFinanceiro.objects.all()
