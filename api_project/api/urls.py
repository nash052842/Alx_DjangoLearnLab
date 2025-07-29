from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django , urls import path, include
from rest_framework.import DefaultRounter
from.views import BookViewSet

router=DefaultRounter()

router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns= [
    
    path(DefaultRouter()", "router.urls),
]