from .models import social_media as Social
def social_dict(request):
    social = {}
    urls = Social.objects.all()
    for url in urls:
        social[url.key] = url.url
    return {'SOCIAL':social}