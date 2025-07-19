from django.http import HttpResponse
from .models import Book

def list_books(request):
    books = Book.objects.all()
    output = ""

    for book in books:
        output += f"{book.title} by {book.author.name}<br>"

    return HttpResponse(output)


from django.http import HttpResponse
from .models import Book

from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context




