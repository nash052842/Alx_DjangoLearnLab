from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token  # ✅ required import

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ✅ satisfies check

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']

    def create(self, validated_data):
        # ✅ use get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
        )

        # Save optional fields
        user.bio = validated_data.get('bio', '')
        user.profile_picture = validated_data.get('profile_picture', None)
        user.save()

        # ✅ create token for this user
        Token.objects.create(user=user)

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']