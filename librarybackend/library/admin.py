from django.contrib import admin
from .models import Publisher, Author, Book, Publication


@admin.register(Publisher)
class AdminPublisher(admin.ModelAdmin):
    fields = ["name"]


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    fields = ["name"]


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    fields = ["title", "photo"]


@admin.register(Publication)
class AdminPublication(admin.ModelAdmin):
    fields = ["book", "publish_company", "authors"]
