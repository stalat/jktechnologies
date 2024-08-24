from django.urls import path
from bookmanagement import views as book_views

urlpatterns = [
    path('books', book_views.BookCreateAPIView.as_view(), name='bookcreateapiview'),
    path('books/<int:pk>', book_views.BookFetchUpdateView.as_view(), name='bookfetchupdate'),
    path('books/<int:id>/reviews/', book_views.RatingCreateAPIView.as_view(), name='reviewcerateapiview'),
    path('books/<int:id>/reviews/<int:pk>/', book_views.RatingFetchUpdateView.as_view(), name='reviewfetchupdate'),
    path('books/<int:id>/summary/', book_views.BookRatingAPIView.as_view(), name='aggregatedrating'),
]
