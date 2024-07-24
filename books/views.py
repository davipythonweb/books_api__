from rest_framework import generics
from books.models import Book

from books.serializers import BookSerializer, BookListDetailSerializer


class BookCreateListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListDetailSerializer
        return BookSerializer
    
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListDetailSerializer
        return BookSerializer