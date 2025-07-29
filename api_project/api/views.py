from rest_framework .import generics

from.models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):

    queryset =Book.object.all()

    serilaizer_class = BookSerializer

    
from rest_framework import serializer
from .models import Book
class Bookserializer(serializer.ModelSerializer):
    
    class meta:
        model=Book
        field = ["id","title","author","publish_date"]

from rest_framework import viewsets
from .models import Book
from serializers import Bookserializer

class BookViewSet(viewsets.ModelviewSet):
queryset = Book.objects.all()
serializer_Class= BookSerializer
