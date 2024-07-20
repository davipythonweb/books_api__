from rest_framework import serializers
from knowledge_area.models import Knowledge_Area

class KnowledgeAreaSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge_Area
        fields = '__all__'