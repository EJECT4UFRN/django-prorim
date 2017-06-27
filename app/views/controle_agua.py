from rest_framework import viewsets
from app.models import ControleAgua
from app.serializers import ControleAguaSerializer, PureControleAguaSerializer, FileControleAguaSerializer
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from djangorestframework_camel_case.parser import CamelCaseJSONParser


class ControleAguaView(viewsets.ModelViewSet):
    queryset = ControleAgua.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return PureControleAguaSerializer
        else:
            return ControleAguaSerializer


class FileControleAguaView(viewsets.ModelViewSet):
    queryset = ControleAgua.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileControleAguaSerializer
