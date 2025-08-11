from importlib.resources import contents
from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    published_date=models.DateField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
def __str__(self):
   return self.title
    
