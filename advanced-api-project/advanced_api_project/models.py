from django.db import models

class Author(models.Model):
    Author = models.CharField(max_length=100)
def __str__(self.name)
    return self.name

class Book(models.Models):
    title = models.CharField(max_length=255)
    author = models.ForeignKeyOneToMany(author_on_delete= models.CASCADE,related_name='book')
    published_year = models.IntegerField()
def __str__(self):
    return self.title