>>> book = Book.objects.get(title="1984")
>>> print(book.title)
1984
>>> print(book.author)
George Orwell
>>> print(book.publication_year)
1949