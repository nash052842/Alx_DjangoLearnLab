import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  
        return Book.objects.filter(author=author)      
    except Author.DoesNotExist:
        return []

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

if __name__ == "__main__":
    author_name = "Jane Austen"
    library_name = "Central Library"

    print(f"Books by {author_name}:")
    for book in get_books_by_author(author_name):
        print(f" - {book.title}")

    print(f"\nBooks in {library_name}:")
    for book in list_books_in_library(library_name):
        print(f" - {book.title}")

    librarian = get_librarian_for_library(library_name)
    if librarian:
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    else:
        print(f"\nNo librarian found for {library_name}")
