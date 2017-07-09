from rest_framework import viewsets
from app.models import Secao
from app.serializers import SecaoSerializer, ShallowSecaoSerializer


class SecaoView(viewsets.ModelViewSet):
    queryset = Secao.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or  self.action == 'partial_update':
            return ShallowSecaoSerializer
        return SecaoSerializer
