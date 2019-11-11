from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
# Create your models here.

class ContactSpeaker(models.Model):
    first_name=models.CharField(
        verbose_name='nombre',
        max_length=100,
        validators=[
            RegexValidator(
                regex='^([A-Za-z\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff\s]*)$',
                message='Este campo no puede contener numeros'
                )])
    last_name=models.CharField(
        verbose_name='apellido',
        max_length=100,
        validators=[
            RegexValidator(
                regex='^([A-Za-z\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff\s]*)$',
                message='Este campo no puede contener numeros'
                )])
    job_title=models.CharField(
        verbose_name='titulo',
        max_length=100, 
        validators=[
            RegexValidator(
                regex='^([A-Za-z\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff\s]*)$',
                message='Este campo no puede contener numeros'
                )])
    email=models.EmailField(verbose_name='email')
    message=models.TextField(verbose_name='mensaje',max_length=256)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'mensaje recibido'
        verbose_name_plural = 'mensajes'

    def __str__(self):
        return self.email
    