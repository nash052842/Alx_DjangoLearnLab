
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
>>> Book.objects.all()
<QuerySet []>
>>>
