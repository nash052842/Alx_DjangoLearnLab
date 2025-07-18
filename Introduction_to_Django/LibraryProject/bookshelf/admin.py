from django.contrib import admin

from.import Book

@admin.register(Book)

class BookAdmin(admin.modelAdmin)
    
list_daiplay=('title',author',publication_year') #column shown in the list

list_filter= ('publication_year','author')      #sidebar filter
             
search_field=('title','author')                 #saerch bar filter
    
