
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),                # List all books
    path('books/create/', BookCreateView.as_view(), name='book-create'),     # Create a new book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),   # Retrieve a single book by id
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  # Update book by id
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete book by id
    path('books/update/', BulkBookUpdateView.as_view(), name='book-bulk-update'),
    path('books/delete/', BulkBookDeleteView.as_view(), name='book-bulk-delete'),

]
