from rest_framework import viewsets

from .serializers import TestSerializer
from .models import Test


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all().order_by('name')
    serializer_class = TestSerializer
