# Generated by Django 3.1.13 on 2022-03-31 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_news_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short_description',
            field=models.CharField(max_length=300),
        ),
    ]
