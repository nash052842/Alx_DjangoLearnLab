from pyexpat import model
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"





from django.contrib.auth.models import AbstractUser

from django.db import models

class CustomUser(AbstractUser):
    date_of_birth=model.IntegerField()
    profile_photo =model.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)mmage_field
def __str__(self):

    return self.username


from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)





from django.contrib.auth.models import Permission
class Meta:
    Permission=[ 
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
    
def __str_(self):
    return self.title
class Command(BaseCommad)
    help = "Sets up user groups and assigns permissions."
    # 📁 management/commands/setup_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = "Sets up user groups and assigns permissions."

    def handle(self, *args, **kwargs):
        book_model = apps.get_model('bookshelf', 'Book')

        perms = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, codename_list in perms.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.clear()
            for codename in codename_list:
                permission = Permission.objects.get(codename=codename, content_type__app_label="bookshelf")
                group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS("Groups and permissions successfully set up."))

