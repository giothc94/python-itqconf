from django.contrib import admin
from .models import social_media

# Register your models here.
@admin.register(social_media)
class SocialMediaAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')