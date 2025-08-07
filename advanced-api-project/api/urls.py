from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookViewSet,
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
)

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    # Optional: Explicit class-based views (only if you need them for other purposes)
    path('book/', BookListView.as_view(), name='book-list'),
    path('book/create/', BookCreateView.as_view(), name='books-create'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='books-detail'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='books-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='books-delete'),
]




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
