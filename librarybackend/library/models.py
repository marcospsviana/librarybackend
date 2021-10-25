from django.db import models

# Create your models here.


class PublishCompany(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Publishers"


class Author(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Authors"


class Book(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=200, null=False)
    photo = models.URLField(verbose_name="book_cover", max_length=500, null=True)
    authors = models.ManyToManyField(Author, through="Publications")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Books"


class Publications(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publish_company = models.ForeignKey(PublishCompany, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book}"

    class Meta:
        verbose_name_plural = "Publications"
