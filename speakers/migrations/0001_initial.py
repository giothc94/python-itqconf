# Generated by Django 2.2.7 on 2019-11-10 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200, verbose_name='titulo')),
                ('development_stack', models.CharField(max_length=200, null=True, verbose_name='tecnologias')),
                ('facebook_url', models.URLField(blank=True, verbose_name='facebook')),
                ('instagram_url', models.URLField(blank=True, verbose_name='instagram')),
                ('github_url', models.URLField(blank=True, verbose_name='github')),
                ('twitter_url', models.URLField(blank=True, verbose_name='twitter')),
                ('biography', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='speakers', verbose_name='imagen de perfil')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nombre de usuario')),
            ],
            options={
                'verbose_name': 'speaker',
                'verbose_name_plural': 'speakers',
            },
        ),
    ]