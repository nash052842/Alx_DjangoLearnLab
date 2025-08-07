#from django.urls import path, include
#from rest_framework.routers import DefaultRouter
from .views import (
    BookViewSet,
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
)

#router = DefaultRouter()
#router.register(r'books', BookViewSet, basename='book')

#urlpatterns = [
    path('', include(router.urls)),
    # Optional: Explicit class-based views (only if you need them for other purposes)
    path('books/', BookListView.as_view(), name='book-list-cbv'),
    path('books/create/', BookCreateView.as_view(), name='book-create-cbv'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail-cbv'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update-cbv'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete-cbv'),
]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),  # no explicit update/delete paths here!
]
