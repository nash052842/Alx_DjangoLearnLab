from django.urls import path
from.import views

urlpattern=[
    path('register/' views.register_view,name='register')
    path('login/'views.login_view,name='login')
    path('logout/'views.logout_view,name='logout')
    path('profile/' views.profile_view,name= 'profile')
]

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View one post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
]




