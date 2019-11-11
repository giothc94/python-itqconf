# Generated by Django 2.2.7 on 2019-11-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSpeaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='apellido')),
                ('job_title', models.CharField(max_length=100, verbose_name='titulo')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('message', models.TextField(verbose_name='mensaje')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'mensaje recibido',
                'verbose_name_plural': 'mensajes',
            },
        ),
    ]
