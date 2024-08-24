from django.contrib import admin
from bookmanagement.models import Books, Author, Reviews

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_published', 'genre')
    list_filter = ('genre', 'year_published')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_country')

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating')