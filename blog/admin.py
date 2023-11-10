from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Blog, Comment
# Register your models here.

@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('title', 'author', 'published')
    list_per_page = 10
    list_display_links = ('title', 'author')
    list_filter = ('title',)
    list_editable = ('published',)

@admin.register(Comment)
class BlogAdmin(ModelAdmin):
    list_display = ('author_comment', 'post', 'date_created')
    list_filter = ('post',)
    list_per_page = 10
    list_display_links = ('post', 'author_comment')

