from django.db import models

# Create your models here.


class PublishCompany(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, null=False)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'names'

class Author(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, null=False)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'names'


class Book(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=200, null=False)
    photo = models.ImageField(name='image')
    author = models.ManyToManyField(Author)
    publish_company = models.ManyToManyField(PublishCompany)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'titles'
