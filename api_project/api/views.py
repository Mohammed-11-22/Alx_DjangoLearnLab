from django.shortcuts import render
from rest_framework.generics import ListAPIView # type: ignore
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
