from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='George Orwell')

        # Test data
        self.book1 = Book.objects.create(title='1984', author=self.author, published_year=2000)
        self.book2 = Book.objects.create(title='Animal Farm', author=self.author, published_year=2000)
        self.book3 = Book.objects.create(title='Django for APIs', author=self.author, published_year=2020)

        self.client = APIClient()

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-list')
        data = {
            'title': 'Homage to Catalonia',
            'author': self.author.id,
            'published_year': 1938
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        url = reverse('book-list')
        data = {
            'title': 'Keep the Aspidistra Flying',
            'author': self.author.id,
            'published_year': 1936
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.put(url, {
            'title': 'Nineteen Eighty-Four',
            'author': self.author.id,
            'published_year': 1949
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Nineteen Eighty-Four')

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-detail', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_filter_books_by_year(self):
        url = reverse('book-list') + '?published_year=2020'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        for book in response.data:
            self.assertEqual(book['published_year'], 2020)

    def test_search_books(self):
        url = reverse('book-list') + '?search=Django'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        for book in response.data:
            self.assertIn('Django', book['title'])

    def test_order_books_by_year(self):
        url = reverse('book-list') + '?ordering=published_year'
        response = self.client.get(url)
        years = [book['published_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
