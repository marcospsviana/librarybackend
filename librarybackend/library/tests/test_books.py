from django.shortcuts import reverse
import pytest
from librarybackend.library.models import Publications, Author, PublishCompany, Book
from model_bakery import baker


@pytest.fixture
def publication(db):
    book_set = baker.prepare(Book, _quantity=3, _save_related=True)
    company_set = baker.prepare(PublishCompany, _quantity=3, _save_related=True)
    authors_set = baker.prepare(Author, _quantity=3, _save_related=True)
    return baker.make(Book)


@pytest.fixture
def publications(db):
    # book_set = baker.prepare(Book, _quantity=3, _save_related=True)
    # company_set = baker.prepare(PublishCompany, _quantity=3, _save_related=True)
    authors_set = baker.prepare(Author, _quantity=3, _save_related=True)
    return baker.make(
        Publications,
        _bulk_create=True,
        make_m2m=True,
        author=authors_set,
        book=baker.make(Book),
        publish_company=baker.make(PublishCompany),
    )


@pytest.fixture
def resp(client, publication, db):
    resp_book = client.get(
        reverse("library:books"), kwargs={"publications": publication}
    )
    return resp_book


def test_status_code_200_endpoint_books(client, resp):
    assert resp.status_code == 200


def test_response_data_book_list(resp, publications):
    for b in publications:
        assert resp, b.title


def test_response_data_book_json(resp, publications):
    for b in books:
        assert resp, {
            "id": b.id,
            "title": b.title,
            "publisher_company": b.publish_company,
            "photo": b.photo,
            "authors": b.author,
        }


def test_len_list_books(resp, publications):
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
