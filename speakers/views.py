from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect,reverse, render, get_object_or_404
from django.urls import reverse_lazy
from .models import Speaker
from .forms import CreateSpeakerForm

class SpeakerDetailView(DetailView):

    queryset = Speaker.objects.all()

    # template_name='speakers/about-speaker.html'

    def get_object(self):
        speaker = super().get_object()
        return speaker

class UpdateSpeaker(UpdateView):
    model = Speaker
    form_class = CreateSpeakerForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('index')

class CreateSpeaker(CreateView):
    model = Speaker
    form_class = CreateSpeakerForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        user = User.objects.get(id=self.request.user.id)
        obj.user = user
        return super().form_valid(form)