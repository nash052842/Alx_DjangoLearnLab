>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book)
Book object (1)
>>> print(book.title, book.author, book.publication_year)       
1984 George Orwell 1949