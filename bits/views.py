from django.shortcuts import render
from .models import Bit
from rest_framework import viewsets, permissions
from .serializers import BitSerializer

# Create your views here.
class BitViewSet(viewsets.ModelViewSet):
    queryset = Bit.objects.all()
    serializer_class = BitSerializer
    permission_classes = [permissions.AllowAny]