from librarybackend.library.models import Book
from typing import List


def list_all_books() -> List[Book]:
    return list(Book.objects.order_by("title").all())


def book_by_id(id) -> Book:
    return Book.objects.filter(id=id).first()
