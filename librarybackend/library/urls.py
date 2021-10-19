from django.urls import path
from librarybackend.library.views import Books

app_name = "library"
urlpatterns = [
    path("books/", Books.as_view(), name='books'),
    ]
