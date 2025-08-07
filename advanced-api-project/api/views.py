from rest_framework import generics
import serializer
from . import Bookserializer
from . import models

class bookCraeteView(generics.CreateAPIView):
    
    queryset = Book.obj.all()
    serializer_class = serializer

class bookDeleteView(generics.DestroyAPIView):
    queryset = Book.obj.all()
    serilaizer_class = serializer

class bookUpdateView(generics.BookupdateView):
    queryset= Book.obj.all ()
    serializer_class = serializer

class BookListRetriveView(generics.BookretriveAPIview):
    queryset= Book.obj.all()
    serializer_class = serializer
    
class BookListDeatailView(generics.BookdeatilaAPIview):
    quryset = Book.obj.all()
    serializer_class =serializer

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializer import BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can create



class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can update

    
    
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
  
