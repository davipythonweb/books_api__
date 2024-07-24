from rest_framework import generics
from writers.models import Writer

from writers.serializers import WriterSerializer


class WriterCreateListView(generics.ListCreateAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class WriterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer