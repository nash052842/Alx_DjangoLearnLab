from pyexpat import model
from typing import Self
from django.db import models

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# relationship_app/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can edit book details"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title



from django.contrib.auth.models import AbstractUser

from django.db import models

class customUser(AbstractUser):
    date_of_birth=model.IntegerField()
    profile_photo =model.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)mmage_field
def __str__(self):

    return self.username

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy

class customerUsermanager(BaseUserManager):
    use_in_migration=True
def create__user(self,username,email,=none,password=none ** extra_field):
    if its not username:
        raise valueError("the username must be set")
    email=self.normalize_email(email)
    User.selfmodel(username=username,email=email,**extra_fields)
    User.set_password
    User.save (using=self._db)
    return User
def create superUser(Self,Username,email=none,password=none,**extra_field)
    extra_field.setdefult("is staff,True")
    extra_fields.setdefault("is_superuser,"True)
    extra_fields.setdefault("is_active,"True)
    
    if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

