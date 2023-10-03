from .models import Tourdate
from rest_framework import serializers

class TourdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourdate
        fields = '__all__' 
