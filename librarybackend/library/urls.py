from django.urls import path
from librarybackend.library.views import books
app_name = 'library'
urlpatterns = [
    path('books/', books, name='books')
]