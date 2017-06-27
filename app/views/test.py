from rest_framework import viewsets
from app.models import TestModel
from app.serializers import TestSerializer


class TestView(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
