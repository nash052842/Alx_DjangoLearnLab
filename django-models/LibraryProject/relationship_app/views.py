from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic.detail import DetailView  # for CBV

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View to show a specific library with its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

