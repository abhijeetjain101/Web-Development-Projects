# Generated by Django 3.2.6 on 2022-01-06 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Newsapp',
            new_name='NewsContent',
        ),
    ]