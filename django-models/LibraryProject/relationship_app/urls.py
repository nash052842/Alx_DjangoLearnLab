from django.urls import path
from .views import list_books, LibraryDetailView  # Make sure these are defined in views.py

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]


