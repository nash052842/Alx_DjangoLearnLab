from django.contrib import admin
from .models import Post, Comment

# Inline for comments
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Number of empty comment fields shown
    fields = ('author', 'content', 'created_at')
    readonly_fields = ('created_at',)

# Post admin (this replaces your old BlogAdmin)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [CommentInline]  # Show comments inline on Post admin page

# Comment admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'updated_at')
    search_fields = ('content',)
    list_filter = ('created_at', 'author')
