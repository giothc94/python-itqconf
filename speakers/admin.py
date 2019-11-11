from django.contrib import admin
from .models import Speaker
# Register your models here.
@admin.register(Speaker)
class SpeakersAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')
    # list_display=(
    #     'user',
    #     'job_title',
    #     'picture',
    # )
    
    # search_fields=(
    #     'user__email',
    #     'user__first_name',
    #     'user__last_name'
    # )

    # list_filter = (
    #     'created',
    #     'updated',
    #     'user__is_active',
    # )