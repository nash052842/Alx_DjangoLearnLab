from django.urls import path
from.import views
(
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpattern=[
    path('register/' views.register_view,name='register')
    path('login/'views.login_view,name='login')
    path('logout/'views.logout_view,name='logout')
    path('profile/' views.profile_view,name= 'profile')

]

urlpatterns = [
    path('posts/',PostListView.as_view(), name='post-list'),
    path('posts/new/',PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/',PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
]