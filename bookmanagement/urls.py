from django.urls import path
from bookmanagement.views import BookCreateAPIView, BookFetchUpdateView

urlpatterns = [
    path('books', BookCreateAPIView.as_view(), name='bookcreateapiview'),
    path('books/<int:pk>', BookFetchUpdateView.as_view(), name='bookfetchupdate'),
]
