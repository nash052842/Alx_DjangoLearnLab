from rest_framework.routers import DefaultRouter
from.views import PostViewSet, CommentViewSet
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
urlpatterns = [
    path('post/<int:post_id>/comments/', views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-comments'),
    path('post/<int:post_id>/comments/<int:pk>/', views.CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-comment-detail'),
    path('', include(router.urls)),

]
