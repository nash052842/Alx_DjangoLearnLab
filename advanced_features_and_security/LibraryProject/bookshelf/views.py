
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library  # make sure 'Library' is a valid model

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

def list_books(request):
    return render(request, 'list_books.html')


