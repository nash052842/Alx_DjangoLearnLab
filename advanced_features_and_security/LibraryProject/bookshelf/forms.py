from django import forms

class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)
