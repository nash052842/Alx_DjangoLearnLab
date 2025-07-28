from rest_framework import serializers

from.models import Book
from api import models

class BookSerializer(serializers.Modelserializer):
    class meta:
        model=Book
        field="__all__"
