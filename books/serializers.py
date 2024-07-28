from rest_framework import serializers
from books.models import Book

from django.db.models import Avg

from matters.serializers import MatterSerializer
from knowledge_area.serializers import KnowledgeAreaSerilizer


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1400:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1400.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracteres.')
        return value
    
class BookListDetailSerializer(serializers.ModelSerializer):
    matter = MatterSerializer(many=True)
    knowledge_area = KnowledgeAreaSerilizer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'knowledge_area', 'matter', 'release_date','writer','publishing_company','resume']

    
    def get_rate(self, obj):
        average_rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if average_rate:
            return round(average_rate, 1)  



class BookStatsSerializer(serializers.Serializer):
    total_books = serializers.IntegerField()  
    books_by_knowledge_area = serializers.ListField()  
    total_reviews = serializers.IntegerField()  
    average_stars = serializers.FloatField()  


