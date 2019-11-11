from django import template
from footer_pages.models import Page

register=template.Library()

@register.simple_tag
def get_page_footer_list():
    pages = Page.objects.all()
    return pages