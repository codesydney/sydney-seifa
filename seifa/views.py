from rest_framework import generics
from .models import Seifa
from .serializers import SeifaSerializer

class SeifaList(generics.ListCreateAPIView):
    queryset = Seifa.objects.all()
    serializer_class = SeifaSerializer
