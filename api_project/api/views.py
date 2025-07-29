from rest_framework .import generics

from.models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):

    queryset =Book.object.all()

    serilaizer_class = BookSerializer
    
from rest_framework import serializer
from .models import Book
class Bookserializer(serializers.ModelSerializer):
    
    class meta:
        model=Book
        field = ["id","title","author","publish_date"]

from rest_framework import viewsets
from .models import Book
from serializers import Bookserializer

classBookviewset = (viewsets.Modelkviewset):
queryset= Book.object.all()
serializer_Class= BookSerializer
