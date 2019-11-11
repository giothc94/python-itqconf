from django.urls import path
from .views import SpeakerDetailView,CreateSpeaker,UpdateSpeaker

urlpatterns = [
    path('<int:pk>/',SpeakerDetailView.as_view(),name='speaker'),
    path('add/',CreateSpeaker.as_view(),name='create-speaker'),
    path('update/<int:pk>/',UpdateSpeaker.as_view(),name='update-speaker'),
]