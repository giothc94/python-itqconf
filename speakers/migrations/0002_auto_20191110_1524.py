# Generated by Django 2.2.7 on 2019-11-10 20:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='biography',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
