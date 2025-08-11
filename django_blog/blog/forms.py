from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Provide a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
def save(self,commit=True):
    user=super().save(commit=False)
    user . email = self.cleaned_date("email")
    if commit:
        user.save
    return user
    



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
