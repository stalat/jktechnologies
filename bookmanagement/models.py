from django.db import models
from django.contrib.auth.models import User

class CreateUpdate(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Author(CreateUpdate):
    author_name = models.CharField(max_length=200)
    author_details = models.TextField(null=True, blank=True)
    author_country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.author_name


class Books(CreateUpdate):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, related_name='book_author')
    year_published = models.CharField(max_length=4)
    summary = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Reviews(CreateUpdate):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(null=True, blank=True)
    rating = models.IntegerField()