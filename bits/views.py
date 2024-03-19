from django.shortcuts import render
from .models import Bit
from rest_framework import viewsets, permissions
from .serializers import BitSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.http import HttpResponseForbidden

# Create your views here.
class BitViewSet(viewsets.ModelViewSet):
    queryset = Bit.objects.all()
    serializer_class = BitSerializer
    permission_classes = [permissions.AllowAny]  # Default permission

    def update(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"detail": "You do not have permission to edit this item."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"detail": "You do not have permission to edit this item."}, status=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"detail": "You do not have permission to delete this item."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
