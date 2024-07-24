from rest_framework import serializers
from writers.models import Writer

class WriterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Writer
        fields = '__all__'