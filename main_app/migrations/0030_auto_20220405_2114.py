# Generated by Django 3.1.13 on 2022-04-05 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0029_useraccount_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydetails',
            old_name='tel2',
            new_name='tel_lab',
        ),
        migrations.AddField(
            model_name='companydetails',
            name='tel_welcome',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]