from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class BlogsAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')