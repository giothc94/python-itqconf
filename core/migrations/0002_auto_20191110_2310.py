# Generated by Django 2.2.7 on 2019-11-11 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactspeaker',
            name='first_name',
            field=models.TextField(max_length=100, verbose_name='nombre'),
        ),
    ]
