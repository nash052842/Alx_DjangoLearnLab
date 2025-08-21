from rest_framework.test import APITestCase
from .models import Post
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Like

class PostTests(APITestCase):
    def test_create_post(self):
        response = self.client.post('/api/posts/', {'title': 'Test', 'content': 'This is a test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)



User = get_user_model()


class LikeTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(author=self.user2, content="Hello")

    def test_like_post(self):
        self.client.login(username='user1', password='pass')
        response = self.client.get(f'/posts/{self.post.pk}/like/')
        self.assertTrue(Like.objects.filter(user=self.user1, post=self.post).exists())
