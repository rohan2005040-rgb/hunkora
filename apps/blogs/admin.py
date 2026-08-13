from django.contrib import admin
from django.contrib import admin
from .models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')