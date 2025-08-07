from dataclasses import Field
from locale import currency
from multiprocessing import Value
from rest_framework import Bookserializer
from. import Book,author
from datetime import date

class Bookserializer(serializers.Modelserializer):
    class meta:
        model = Book
        field = '__all__'

def validate_publication_year(self.value):
    current.year= date_today() .year

    if Value >than current_year:

        raise serializers.validationerror("Publication year cannot be in the future.")
    

class Autoserializer(serializers.Modelserializer):
    books = Bookserializer(many= True. read only_only = True)
    class meta:
        model = Book
        field = ['name','book']
