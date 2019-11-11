from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField
# Create your models here.
class Page(models.Model):
    title=models.CharField(
        verbose_name="Título", 
        max_length=100,
        validators=[
            RegexValidator(
                regex='^([A-Za-z\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff\s]*)$',
                message='Este campo no puede contener numeros'
                )])
    content=RichTextField(verbose_name="Contenido")

    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de cración")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="página"
        verbose_name_plural="páginas footer"

    def __str__(self):
        return self.title