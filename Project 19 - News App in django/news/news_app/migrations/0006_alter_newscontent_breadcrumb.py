# Generated by Django 3.2.9 on 2022-01-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0005_auto_20220111_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscontent',
            name='breadcrumb',
            field=models.URLField(blank=True, null=True),
        ),
    ]
