from django.urls import path
from librarybackend.library.views import Books, BookDelete

app_name = "library"
urlpatterns = [
    path("books/", Books.as_view(), name="books"),
    path("books/<int:id>", BookDelete.as_view(), name="delete"),
]
