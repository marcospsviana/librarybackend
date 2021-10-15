from .models import Book
import json

# Create your views here.


def books():
    books_list = Book.objects.order_by("title").all()
    books = [
        {
            "id": 1,
            "title": book.title,
            "publisher_company": book.publish_company,
            "photo": book.photo,
            "authors": [author.name for author in book.author],
        }
        for book in books_list
    ]
    return json.dumps(books)
