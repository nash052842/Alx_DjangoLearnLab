from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):

        return self.name
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        self.title

class Library(models.Model):
    name=models.CharField(max_length=255)
    books = models.ManyToManyField('Book', related_name='libraries')
    def __str__(self):
      return  self.name
    

class Librarian(models.Model):
    name=models.CharField(max_length=255)
    Library=models.OneToOneField("Library", on_delete=models.CASCADE, related_name='Librarian')
    def __str__(self):
        return self.name
