# -*- coding: utf-8 -*-
from dateutil.parser import parse
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from app.models import Secao
from app.serializers import SecaoSerializer, ShallowSecaoSerializer


class SecaoView(viewsets.ModelViewSet):
    queryset = Secao.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowSecaoSerializer
        return SecaoSerializer

    def get_queryset(self):
        if self.action == 'list':
            query = Secao.objects.all()
            filtro = self.request.query_params
            if filtro:
                if 'sala' in filtro:
                    query = query.filter(sala=filtro['sala'])
                    if 'data' in filtro:
                        data = parse(filtro['data'])
                        query = query.filter(
                            data__year=data.year,
                            data__month=data.month,
                            data__day=data.day
                            )
                        if 'periodo' in filtro:
                            query = query.filter(
                                periodo=filtro['periodo']
                                )
                            return query
            return None
        return Secao.objects.all()

    def perform_create(self, serializer):
        print(serializer.validated_data)
        is_not_unique = Secao.objects.filter(
            data=serializer.validated_data['data'],
            sala=serializer.validated_data['sala'],
            periodo=serializer.validated_data['periodo']
            )
        if is_not_unique:
            alert = 'Essa seção já existe.'
            raise serializers.ValidationError(
                {'secao': alert}
            )
        else:
            serializer.save()
