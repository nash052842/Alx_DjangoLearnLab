from django.urls import path
from .views import PostByTagListView
from .views import search_posts
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
path('post/<int:pk>/comments/<int:comment_pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
path('post/<int:pk>/comments/<int:comment_pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

from .views import SearchResultsView
from taggit.views import TaggedObjectList

urlpatterns += [
    path('search/', SearchResultsView.as_view(), name='post-search'),
    path('tags/<slug:tag>/', PostListView.as_view(), name='posts-by-tag'),
]

def get_queryset(self):
    tag = self.kwargs.get('tag')
    if tag:
        return Post.objects.filter(tags__name__in=[tag])
    return Post.objects.all().order_by('-published_date')

from .views import TaggedPostListView

urlpatterns = [
    path('tags/<slug:slug>/', TaggedPostListView.as_view(), name='posts-by-tag'),

path('search/', search_posts, name='search-posts'),
path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts-by-tag"),
]





