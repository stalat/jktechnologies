from django.shortcuts import render
from bookmanagement.models import Books, Reviews
from bookmanagement.serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class BookCreateAPIView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookFetchUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer