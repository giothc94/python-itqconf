from django.contrib import admin
from .models import ContactSpeaker
# Register your models here.
@admin.register(ContactSpeaker)
class ContactSpeakerAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')