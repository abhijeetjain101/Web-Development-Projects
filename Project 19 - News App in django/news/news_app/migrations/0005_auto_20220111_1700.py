# Generated by Django 3.2.6 on 2022-01-11 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_auto_20220111_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='newscontent',
            name='tags',
            field=models.ManyToManyField(blank=True, to='news_app.Tag'),
        ),
    ]
