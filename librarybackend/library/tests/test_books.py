from django.shortcuts import reverse
import pytest
from librarybackend.library.models import Book
from model_bakery import baker


@pytest.fixture
def book(db):
    return baker.make(Book, _bulk_create=True)


@pytest.fixture
def books(db):
    return baker.make(Book, _bulk_create=True, _quantity=3)


@pytest.fixture
def resp(client, books):
    resp_book = client.get(reverse("library:books"), kwargs={"book": book})
    return resp_book


def test_status_code_200_endpoint_books(client, resp):
    assert resp.status_code == 200


def test_response_data_book_list(resp, books):
    for b in books:
        assert resp, b.title


def test_response_data_book_json(resp, books):
    for b in books:
        assert (
            resp,
            {
                "id": b.id,
                "title": b.title,
                "publisher_company": b.publish_company,
                "photo": b.photo,
                "authors": b.author,
            },
        )


def test_len_list_books(resp, books):
    assert 3 == len(books)


@pytest.mark.django_db
def test_delete_book():
    book = Book.objects.create(title="Um livro de teste")
    query = Book.objects.all()
    assert len(query) == 1
    assert book.title == "Um livro de teste"
    book = Book.objects.get(title=book.title).delete()
    assert book == (1, {"library.Book": 1})
    query = Book.objects.all()
    assert len(query) == 0

