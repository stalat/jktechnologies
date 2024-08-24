from rest_framework import serializers
from bookmanagement.models import Books, Reviews

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'