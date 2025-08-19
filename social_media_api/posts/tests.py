from rest_framework.test import APITestCase
from .models import Post

class PostTests(APITestCase):
    def test_create_post(self):
        response = self.client.post('/api/posts/', {'title': 'Test', 'content': 'This is a test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)
