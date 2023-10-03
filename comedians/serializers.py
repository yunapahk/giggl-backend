from .models import Comedian
from rest_framework import serializers

class ComedianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comedian
        fields = '__all__'  
        
