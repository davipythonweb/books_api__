from rest_framework import generics, views, response, status
from books.models import Book

from django.db.models import Count, Avg
from books.serializers import BookSerializer, BookListDetailSerializer, BookStatsSerializer

from reviews.models import Review

from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission



class BookCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListDetailSerializer
        return BookSerializer
    

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListDetailSerializer
        return BookSerializer
    



class BookStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Book.objects.all()  

    def get(self, request):
        total_books = self.queryset.count()  
        books_by_knowledge_area = self.queryset.values('knowledge_area__name').annotate(count=Count('id'))  # Contagem de filmes por gênero
        total_reviews = Review.objects.count()  
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']  

        
        data = {
            'total_books': total_books,
            'books_by_knowledge_area': books_by_knowledge_area,
            'total_reviews': total_reviews,
        
        
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }
        

    
        serializer = BookStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True) 

        return response.Response(
            data=serializer.data,  
            status=status.HTTP_200_OK, 
        )
    