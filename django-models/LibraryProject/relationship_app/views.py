from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library


# ✅ Function-Based View: List all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ✅ Class-Based View: Show details of a library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all books related to this library instance
        context['books'] = self.object.book_set.all()
        return context
