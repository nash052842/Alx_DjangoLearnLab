retrive.md

#retrive book instance
from Bookshelf.import Book
retrive_book=Book.object.get(title="1984")
print(book title,book author,book.publication_year)