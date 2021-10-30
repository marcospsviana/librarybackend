# Generated by Django 3.2.8 on 2021-10-30 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_model_publication_author2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Publications',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Publishers',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Publications',
        ),
        migrations.DeleteModel(
            name='PublishCompany',
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.ManyToManyField(related_name='publications', to='library.Author'),
        ),
        migrations.AddField(
            model_name='publication',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
        migrations.AddField(
            model_name='publication',
            name='publish_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.publisher'),
        ),
    ]
