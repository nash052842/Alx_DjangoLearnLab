from django.db import models
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'picture', 'followers']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data.pop('username'),
            email=validated_data.pop('email'),
            password=validated_data.pop('password'),
            phone_number=validated_data.pop('phone_number'),
            bio=validated_data.pop('bio')
        )
        return user
    def to_representation(self, instance):
        data = super().to_representation(instance)
        refresh = RefreshToken.for_user(instance)
        data['followers'] = instance.followers.count()
        data['access'] = str(refresh)
        return data
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'picture', 'followers']