# Generated by Django 3.1.13 on 2022-03-31 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20220331_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short_description',
            field=models.CharField(max_length=250),
        ),
    ]