from rest_framework .generic import ListAPIView

from.models import Book
from . serializers import BookSerilaizers

class Booklist(ListAPIView):
    queryset =Book.object.all()
    serilaizer= BookSerilaizers
    