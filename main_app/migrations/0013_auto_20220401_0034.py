# Generated by Django 3.1.13 on 2022-04-01 00:34

import ckeditor.fields
from django.db import migrations, models
import main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_companydetails_presentation_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetails',
            name='historique',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companydetails',
            name='historique_image',
            field=models.FileField(default=1, upload_to='', validators=[main_app.validators.validate_file_extension]),
            preserve_default=False,
        ),
    ]
