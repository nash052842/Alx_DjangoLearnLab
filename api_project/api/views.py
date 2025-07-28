from rest_framework .import generic ListAPIView

from.models import Book
from . serializers import BookSerializer

class Booklist(generic.ListAPIView):

    queryset =Book.object.all()

    serilaizer_class = BookSerializer
    