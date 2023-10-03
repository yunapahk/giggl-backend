from .models import Bit
from rest_framework import serializers

class BitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bit
        fields = '__all__' 
