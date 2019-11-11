from django import forms
from .models import Speaker
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CreateSpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = [
            'job_title',
            'development_stack',
            'facebook_url',
            'instagram_url',
            'github_url',
            'twitter_url',
            'biography',
            'picture',
        ]
        widgets={
            'job_title':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Tu experticia, titulo.','type':'text'}),
            'development_stack':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Tecnologias que dominas, separadas por comas.'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Url de tu facebook'}),
            'instagram_url':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Url de tu instagram'}),
            'github_url':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Url de tu github'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Url de tu twitter'}),
            'biography':forms.Textarea(attrs={'class':'form-control mb-2','placeholder':'Tu bio, describete...','rows':5}),
            'picture':forms.FileInput(attrs={'class':'w-100'}),
        }