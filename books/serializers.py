from rest_framework import serializers
from books.models import Book

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
        if len(value) > 100:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracteres.')
        return value
    
class BookListDetailSerializer(serializers.ModelSerializer):
    matters = MatterSerializer(many=True)
    knowledge_area = KnowledgeAreaSerilizer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'knowledge_area', 'matters', 'release_date', 'resume']


