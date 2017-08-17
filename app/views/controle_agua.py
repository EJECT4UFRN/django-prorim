# coding=utf-8
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import ControleAgua
from app.serializers import ControleAguaSerializer, ShallowControleAguaSerializer, FileControleAguaSerializer
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from djangorestframework_camel_case.parser import CamelCaseJSONParser


class ControleAguaView(viewsets.ModelViewSet):
    queryset = ControleAgua.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowControleAguaSerializer
        else:
            return ControleAguaSerializer

    def get_queryset(self):
        query = ControleAgua.objects.all()
        if self.action == 'list':
            filtro = self.request.query_params
            if filtro:
                if 'numeroDoLaudo' in filtro:
                    try:
                        query = query.filter(numero_do_laudo__icontains=filtro['numeroDoLaudo'])
                    except:
                        pass
        return query


class FileControleAguaView(viewsets.ModelViewSet):
    queryset = ControleAgua.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileControleAguaSerializer
    permission_classes = (IsAuthenticated,)
