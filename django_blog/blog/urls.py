from django.urls import path
from . import views (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)


urlpatterns = [
    # ---------- AUTH ROUTES ----------
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # ---------- BLOG POST ROUTES ----------
    path('', views.PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # View one post
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),  # Create a post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Update a post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete a post

    # Comment URLs
    path('post/<int:post_pk>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
