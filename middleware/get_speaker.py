from django.shortcuts import get_object_or_404
from speakers.models import Speaker
def get_speaker_user(get_response):
    # One-time configuration and initialization.

    def middleware(request):

        if request.user:
            try:
                speaker = Speaker.objects.get(user_id=request.user) or None
                request.speaker = speaker
            except Exception:
                request.speaker = None

        response = get_response(request)

        return response

    return middleware