from django.contrib import admin
from .models import PublishCompany, Author, Book, Publications


@admin.register(PublishCompany)
class AdminPublishCompany(admin.ModelAdmin):
    fields = ["name"]


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    fields = ["name"]


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    fields = ["id", "title", "photo"]


@admin.register(Publications)
class AdminPublications(admin.ModelAdmin):
    fields = ["book", "publish_company", "author"]
