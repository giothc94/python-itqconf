from django.db import models
from django.core.validators import RegexValidator
from django.shortcuts import reverse
from speakers.models import Speaker
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    speaker = models.ForeignKey(Speaker,on_delete=models.CASCADE,verbose_name='Autor')
    title = models.CharField(
        verbose_name='Titulo',
        max_length=200,
        unique=True,
        validators=[
            RegexValidator(
                regex='^([A-Za-z\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff\s]*)$',
                message='Este campo no puede contener numeros'
                )])
    subtitle = models.CharField(
        verbose_name='Subtitulo',
        max_length=200,
        validators=[
            RegexValidator(
                regex='^([A-Za-z\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff\s]*)$',
                message='Este campo no puede contener numeros'
                )])
    content = RichTextField(verbose_name='Contenido',max_length=4000)
    picture = models.ImageField(
        verbose_name='imagen del post',
        upload_to='blogs',
    )


    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'blogs'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})