from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('title', 'author', 'published')
    list_filter = ('title',)
    list_editable = ('published',)
