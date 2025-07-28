from rest_framework .import generics

from.models import Book
from .serializers import BookSerializer

class Booklist(generics.ListAPIView):

    queryset =Book.object.all()

    serilaizer_class = BookSerializer
    