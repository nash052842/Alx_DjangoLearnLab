#create book instance
create.md

from bookshelf.models import Book
Book=book.object.create(title="1984" author="George Orwell" pblication_year 1949)
print(Book)

retrive.md

#retrive book instance
from Bookshelf.import Book
retrive_book=Book.object.get(title="1984")
print(book title,book author,book.publication_year)

update.md
#updating Book
from Bookshelf.import Book
update_book= (from"1984" to "nineteen eighty four")

 
delete.md
#delete book
from bookshelf.import Book
Book=book.object.get("title=nineteen eighty four")
book.delete
#confirm deletion by retrieving all books
all books.object=book.object.all
print(all_books)
