from rest_framework import viewsets
from .models import Comedian
from .serializers import ComedianSerializer

class ComedianViewSet(viewsets.ModelViewSet):
    queryset = Comedian.objects.all()
    serializer_class = ComedianSerializer
