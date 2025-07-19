#create.md
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book)
Book object (1)
>>> print(book.title, book.author, book.publication_year)       
1984 George Orwell 1949

#retrive.md
 retrieved_book = Book.objects.get(title="1984")
>>> print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
1984 George Orwell 1949
>>>
#update.md
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)
Nineteen Eighty-Four

#delete.md
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>

