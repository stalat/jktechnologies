from django.contrib import admin
from bookmanagement.models import Books, Author

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_published', 'genre')
    list_filter = ('genre', 'year_published')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_country')