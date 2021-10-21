from .models import Book
from django.http import HttpResponse
from django.views import View


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
