from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')            # Adds sidebar filters
    search_fields = ('title', 'author')           # Show these fields in admin list

admin.site.register(Book, BookAdmin)

    
