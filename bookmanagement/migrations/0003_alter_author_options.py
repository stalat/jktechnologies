# Generated by Django 4.2.15 on 2024-08-25 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanagement', '0002_alter_books_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Author'},
        ),
    ]
