from rest_framework import generics
from writers.models import Writer

from writers.serializers import WriterSerializer


from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class WriterCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class WriterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer