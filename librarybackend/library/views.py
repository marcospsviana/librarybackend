from .models import Book
import json
from django.http import HttpResponse

# Create your views here.


def books(request):
    if request.method == 'GET':
        books_list = Book.objects.order_by("title").all()
        books = [
            {
                "id": 1,
                "title": book.title,
                "publisher_company": book.publish_company,
                "photo": book.photo,
                "authors": book.author,
            }
            for book in books_list
        ]
        return HttpResponse(content=books, headers={"content-type": "application/json"})
    else:
        return 405
