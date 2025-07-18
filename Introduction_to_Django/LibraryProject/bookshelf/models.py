from django.db import models

class Book(models.model):

    title=models.CharField(max_length=200)
    author=models.Charfield(max_length=100)
    publication_year=models.IntegerField()

def __str__(self.Book)

 return f"{self.title} by ({self.author} publication_year)"
