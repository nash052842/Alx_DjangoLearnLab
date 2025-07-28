from django. db import model

from django . contrib.auth import get_user_model

class Book(models.Model):

    title = models.CharFiel(max_length=200)
    author = models.CharField(max_length=100)


    
    
     
