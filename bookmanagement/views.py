from rest_framework.response import Response
from bookmanagement.models import Books, Reviews
from bookmanagement.serializers import BookSerializer, RatingSerializer
from rest_framework import generics
from rest_framework.views import APIView
from bookmanagement.utilities.model_utils import get_book_average_rating
from rest_framework.permissions import IsAuthenticated

class BookCreateAPIView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookFetchUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class RatingCreateAPIView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        book_id = self.kwargs['id']
        return Reviews.objects.filter(book__id=book_id)
    
    def perform_create(self, serializer):
        book_obj = Books.objects.get(id=self.kwargs['id'])
        serializer.save(book=book_obj)

class RatingFetchUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = RatingSerializer

class BookRatingAPIView(APIView):
    def get(self, request, id):
        average_rating = get_book_average_rating(id)
        return Response({'book_id': id, 'average_rating': average_rating})