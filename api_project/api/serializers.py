from rest_framework import serializers

from.models import Book
from api import models

class BookSerializer(serializers.ModelSerializer):
    class meta:
        model=Book
        field="__all__"
