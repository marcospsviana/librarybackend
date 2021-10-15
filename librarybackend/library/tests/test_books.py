from django.shortcuts import reverse
import pytest
from librarybackend.library.models import Book
from model_bakery import baker


@pytest.fixture
def book(db):
    return baker.make(Book, _bulk_create=True, _quantity=3)


@pytest.fixture
def resp(client, book):
    resp_book = client.get(reverse("library:books"), kwargs={"book": book})
    return resp_book


def test_status_code_200_endpoint_books(client, resp):
    assert resp.status_code == 200


def test_response_data_book_list(resp, book):
    for b in book:
        assert (resp, b.title)


def test_response_data_book_json(resp, book):
    for b in book:
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


def test_len_list_books(resp, book):
    assert 3 == len(book)
