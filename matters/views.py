from rest_framework import generics
from matters.models import Matter


class MatterCreateListView(generics.ListCreateAPIView):
    queryset = Matter.objects.all()
    