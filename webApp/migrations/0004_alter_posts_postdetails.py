# Generated by Django 4.2.11 on 2024-04-22 07:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_embvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postdetails',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]