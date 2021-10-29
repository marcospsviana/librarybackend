from .models import Book, PublishCompany, Publications
from django.http import HttpResponse
from django.views import View
import json


class Books(View):
    def get(self, request):
        books_list = Publications.objects.all()

        books = [
            {
                "id": publication.id,
                "title": publication.book.title,
                "publisher_company": publication.publish_company,
                "photo": publication.book.photo,
                "authors": publication.author.select_related(),
            }
            for publication in books_list
        ]

        return HttpResponse(content=books, headers={"content-type": "application/json"})

    def post(self, request):
        # if request.method == 'GET':
        books_list = Book.objects.all()
        books = [
            {
                "id": 1,
                "title": book.title,
                "publisher_company": PublishCompany.objects.get(
                    name=book.publish_company
                ).name,
                "photo": f"{book.photo}",
                "authors": book.author.name,
            }
            for book in books_list
        ]
        return HttpResponse(content=books, headers={"content-type": "application/json"})


class BookDelete(View):
    def delete(self, request, id):
        Book.objects.delete(id)
        return HttpResponse(content=id, headers={"content-type": "application/json"})

    def put(self, request, id):
        if Book.objects.filter(id=id).exists():
            book = Book.objects.filter(id=id)

            print(f"book queryset {book}")

            book_data = self.request
            data_get = b""
            for b in book_data:
                data_get += b

            data_get = json.loads(data_get)

            data_save = Book(
                id=int(data_get["id"]), title=data_get["title"], photo=data_get["photo"]
            )
            Book.objects.update(data_save).where(id=id)
            # author = Author(name=data_get["author"])
            # author.save()
            # author = Author.objects.get(name=data_get["author"])

            data_save.author.set(data_get["author"])
            # company = PublishCompany(name=data_get["publish_company"])
            # company.save()
            # company = PublishCompany.objects.filter(
            #     name=data_get["publis_company"]
            # ).first()
            data_save.publish_company.set(data_get["publish_company"])

            return HttpResponse(
                content=data_get, headers={"content-type": "application/json"}
            )
        else:
            return 404
