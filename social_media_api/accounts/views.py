
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import CustomUserSerializer, UserProfileSerializer
from rest_framework import viewsets
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
        queryset = CustomUser.objects.all()
        serializer_class = CustomUserSerializer
        read_only_fields = ['followers']
        def perform_create(self, serializer):
            serializer.save()

class loginViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    def put(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FollowUserView(APIView):
    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            request.user.profile.following.add(user_to_follow.profile)
            return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
class UnfollowUserView(APIView):
    def post(self, request, user_id):
        try:
            user_to_unfollow = get_user_model().objects.get(id=user_id)
            request.user.profile.following.remove(user_to_unfollow.profile)
            return Response({"message": f"You unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
        except get_user_model().DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
