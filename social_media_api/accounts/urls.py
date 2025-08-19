from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    ProfileView,
    loginViewSet,
    FollowUserView,
    UnfollowUserView,
    CustomUserViewSet,
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)  
router.register(r'auth', loginViewSet, basename='auth')  

urlpatterns = router.urls + [
    path('users/<int:pk>/followers/', FollowUserView.as_view(), name='follow-user'),
    path('users/<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('users/me/', ProfileView.as_view(), name='user-profile'),
    path('users/login/', loginViewSet.as_view({'post': 'create'}), name='user-login'),
    path('users/logout/', loginViewSet.as_view({'post': 'destroy'}), name='user-logout'),
    path('users/register/', CustomUserViewSet.as_view({'post': 'create'}), name='user-register'),
]
