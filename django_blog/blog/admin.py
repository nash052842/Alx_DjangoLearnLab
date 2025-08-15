from django.contrib import admin
from .models import Post, Comment

from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_at')
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
