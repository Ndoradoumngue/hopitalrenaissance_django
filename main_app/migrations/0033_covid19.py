# Generated by Django 3.1.13 on 2022-04-06 10:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0032_message_is_rendez_vous'),
    ]

    operations = [
        migrations.CreateModel(
            name='Covid19',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('is_image', models.BooleanField(default=False)),
                ('on_presentation', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=5000, null=True, unique=True)),
                ('sent_on_on_date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
