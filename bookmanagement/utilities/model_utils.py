from bookmanagement.models import Reviews
from django.db.models import Avg

def get_book_average_rating(book_id):

    return Reviews.objects.filter(book=book_id).aggregate(average_rating=Avg('rating'))['average_rating']
