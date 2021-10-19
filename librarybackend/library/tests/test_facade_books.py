import pytest
from model_bakery import baker
from librarybackend.library.models import Book
from librarybackend.library.facade_books import list_all_books


@pytest.fixture
def books(db):
    return [baker.make(_model=Book, title=t) for t in Book.objects.all()]


def test_list_ordered_books(books):
    assert list(sorted(books, key=lambda book: book.title)) == list_all_books()


def test_book_by_id(books):
    id = 0
    for book in books:
        id += 1
        assert book.id == id
