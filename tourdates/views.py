from rest_framework import viewsets
from .models import Tourdate
from .serializers import TourdateSerializer

class TourdateViewSet(viewsets.ModelViewSet):
    queryset = Tourdate.objects.all()
    serializer_class = TourdateSerializer
