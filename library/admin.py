from django.contrib import admin
from .models import Book


class ListBooks(admin.ModelAdmin):
    list_display = ("id", "name", "author", "category", "description", "release_date", "user_id")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category", 'user_id')
    list_per_page = 10


admin.site.register(Book, ListBooks)
