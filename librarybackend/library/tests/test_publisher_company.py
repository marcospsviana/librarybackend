from django.shortcuts import reverse
import pytest
from librarybackend.library.models import PublishCompany
from model_bakery import baker


@pytest.fixture
def company(db):
    return baker.make(PublishCompany, _bulk_create=True, _quantity=3)


@pytest.fixture
def resp(client, company):
    return client.get(reverse("library:publishcompany"), kwargs={"company": company})


def test_status_code_ok(resp):
    assert resp.status_code == 200
