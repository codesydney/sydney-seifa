from rest_framework import serializers
from .models import Seifa

class SeifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seifa
        fields = '__all__'  # Use '__all__' to serialize all fields