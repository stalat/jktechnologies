from rest_framework import serializers
from bookmanagement.models import Books, Reviews
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(write_only=True)

    class Meta:
        model = Reviews
        fields = ['id', 'book_name', 'user_id', 'review_text', 'rating']
        read_only_fields = ['create_date']

    def create(self, validated_data):
        book_name = validated_data.pop('book_name')
        try:
            book = Books.objects.get(title=book_name)
        except Books.DoesNotExist:
            raise ValidationError(f"Book '{book_name}' does not exist.")

        review = Reviews.objects.create(**validated_data)
        return review
    
    def update(self, instance, validated_data):
        book_name = validated_data.pop('book_name', None)
        book =Books.objects.get(title=book_name)
        instance.book = book
        instance.review_text = validated_data.get('review_text', instance.review_text)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance