from rest_framework import viewsets
from app.models import ChoiceTesteAgua
from app.serializers import ChoiceTesteAguaSerializer


class ChoiceTesteAguaView(viewsets.ModelViewSet):
    queryset = ChoiceTesteAgua.objects.all()
    serializer_class = ChoiceTesteAguaSerializer
