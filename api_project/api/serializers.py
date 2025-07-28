from rest_framework import serializers

from.models import Book
from api import models

class BookSerilization(models.ModelSeriealization):
    class meta:
        model=Book
        field="__all__"
