from django.db import models

# Create your models here.


class PublishCompany(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "names"


class Author(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, null=False)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "names"


class Book(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=200, null=False)
    photo = models.URLField(verbose_name="book_cover", max_length=500, null=True)
    author = models.ManyToManyField(Author, related_name="author")
    publish_company = models.ManyToManyField(
        PublishCompany, related_name="publish_company"
    )

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "titles"
