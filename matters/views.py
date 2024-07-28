from rest_framework import generics
from matters.models import Matter

from matters.serializers import MatterSerializer


from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class MatterCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Matter.objects.all()
    serializer_class = MatterSerializer

class MatterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Matter.objects.all()
    serializer_class = MatterSerializer