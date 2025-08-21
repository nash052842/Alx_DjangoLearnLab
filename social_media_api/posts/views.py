
from rest_framework import viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from posts.models import Post, Comment, Like
from posts.serializers import PostSerializer, CommentSerializer
from posts.permissions import IsOwnerOrReadOnly

from notifications.models import Notification
from notifications.utils import create_notification

from rest_framework import generics  # ✅ Import DRF's generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        Notification.objects.create(
            recipient=comment.post.author,
            sender=self.request.user,
            notification_type='comment',
            post=comment.post
        )


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        following_users = request.user.profile.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')[:10]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created and post.author != request.user:
        create_notification(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )
    return redirect('post_detail', pk=pk)


@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Like.objects.filter(user=request.user, post=post).delete()
    return redirect('post_detail', pk=pk)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)  
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created and post.author != request.user:
        create_notification(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )
    return Response({'message': 'Post liked'}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)  
    Like.objects.filter(user=request.user, post=post).delete()
    return Response({'message': 'Post unliked'}, status=200)

