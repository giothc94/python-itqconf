from django.contrib import admin
from .models import Page
# Register your models here.
@admin.register(Page)
class FooterPagesAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')
