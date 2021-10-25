# Generated by Django 3.2.8 on 2021-10-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_created_models_book_author_publisher_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ManyToManyField(related_name="author", to="library.Author"),
        ),
        migrations.AlterField(
            model_name="book",
            name="publish_company",
            field=models.ManyToManyField(
                related_name="publish_company", to="library.PublishCompany"
            ),
        ),
    ]
