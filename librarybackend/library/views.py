from .models import Book, Author, PublishCompany
from django.http import HttpResponse
from django.views import View
import json

class Books(View):
    def get(self, request):
        # if request.method == 'GET':
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

    def post(self, request):
        # if request.method == 'GET':
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


class BookDelete(View):
    def delete(self, request, id):
        Book.objects.delete(id)
        return HttpResponse(content=id, headers={"content-type": "application/json"})

    def put(self, request, id):
        # if Book.objects.filter(id=id).exists():
        book = Book.objects.filter(id=id)
        book_data = self.request
        data_get = b''
        for b in book_data:
            data_get += b
        # print(f"book ---> {data_get}")
        
        data_get = json.loads(data_get)
        print(f"data get ---> {data_get}")
        # book.update_or_create(id=data_get['id'], title=data_get['title'], photo=data_get['photo'], author=data_get['author'], publish_company=data_get['publish_company'])
        data_save = Book(id=int(data_get['id']), title=data_get['title'], photo=data_get['photo'])
        data_save.save()
        author = Author(name=data_get['author'])
        author.save()
        author = Author.objects.get(name=data_get['author'])

        data_save.author.set(author.id)
        company = PublishCompany(name=data_get['publish_company'])
        company.save()
        company = PublishCompany.objects.filter(name=data_get['publis_company']).first()
        data_save.publish_company.set(company.id)


        return HttpResponse(content=data_get, headers={"content-type": "application/json"})
