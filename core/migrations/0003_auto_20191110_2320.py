# Generated by Django 2.2.7 on 2019-11-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191110_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactspeaker',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
    ]
