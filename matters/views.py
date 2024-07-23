from rest_framework import generics
from matters.models import Matter

from matters.serializers import MatterSerializer

class MatterCreateListView(generics.ListCreateAPIView):
    queryset = Matter.objects.all()
    serializer_class = MatterSerializer