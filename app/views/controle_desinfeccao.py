from rest_framework import viewsets
from app.models import ControleDesinfeccao
from app.serializers import ControleDesinfeccaoSerializer


class ControleDesinfeccaoView(viewsets.ModelViewSet):
    queryset = ControleDesinfeccao.objects.all()
    serializer_class = ControleDesinfeccaoSerializer
    