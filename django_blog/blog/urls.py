from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    register_view,
    login_view,
    logout_view,
    profile_view,
    search_posts,
    SearchResultsView,
    TaggedPostListView,
    PostByTagListView,
)

urlpatterns = [
    # ---------- AUTH ROUTES ----------
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

    # ---------- BLOG POST ROUTES ----------
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View one post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post

    # ---------- COMMENT ROUTES ----------
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # ---------- SEARCH ROUTES ----------
    path('search/', search_posts, name='search-posts'),
    path('search/results/', SearchResultsView.as_view(), name='post-search'),

    # ---------- TAG ROUTES ----------
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts-by-tag"),
    path('tags/<slug:slug>/', TaggedPostListView.as_view(), name='tagged-posts'),
]
