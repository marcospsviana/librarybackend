from .models import Book
import json
from django.http import HttpResponse, response
from django.middleware.csrf import rotate_token
from django.http import HttpResponseNotAllowed
from django.views import View

# Create your views here.
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

# def books(request):
#     request_csrf_token = rotate_token(request)
#     if request.method == 'GET':
#         books_list = Book.objects.order_by("title").all()
#         books = [
#             {
#                 "id": 1,
#                 "title": book.title,
#                 "publisher_company": book.publish_company,
#                 "photo": book.photo,
#                 "authors": book.author,
#             }
#             for book in books_list
#         ]
#         return HttpResponse(content=books, headers={"content-type": "application/json"})
#     elif request.method == 'POST':
#         token = request_csrf_token
#         data_post = request.POST.get('teste')
#         print(data_post)
#         return HttpResponse(200)
#     else:
#         return HttpResponse(f'Method not Allowed {HttpResponseNotAllowed.status_code}')
