from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Speaker(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Nombre de usuario',
    )

    job_title = models.CharField(
        verbose_name='titulo',
        max_length=200,
        validators=[
            RegexValidator(
                regex='^([A-Za-z\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff\s]*)$',
                message='Este campo no puede contener numeros'
                )])

    development_stack = models.CharField(
        verbose_name='tecnologias',
        max_length=50,null=True)
    
    facebook_url = models.URLField(
        verbose_name='facebook',
        max_length=200,
        blank=True
    )
    instagram_url = models.URLField(
        verbose_name='instagram',
        max_length=200,
        blank=True
    )
    github_url = models.URLField(
        verbose_name='github',
        max_length=200,
        blank=True
    )
    twitter_url = models.URLField(
        verbose_name='twitter',
        max_length=200,
        blank=True
    )
    biography = RichTextField(verbose_name='Biografia',blank=True)
    
    picture = models.ImageField(
        verbose_name='imagen de perfil',
        upload_to='speakers',
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name='speaker'
        verbose_name_plural='speakers'
    
    def __str__(self):
        return self.user.email
    
    def development_stack_as_list(self):
        return self.development_stack.split(',')
