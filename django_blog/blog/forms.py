from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .blog.models import Post


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
    



class commentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


from django import forms
from .blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # only let users type the content
        widgets = {
            'content': forms.Text_area(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }

