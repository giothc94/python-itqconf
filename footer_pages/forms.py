from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Page
class CreatePageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'title',
            'content',
        ]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Tu experticia, titulo.','type':'text'}),
            'content':forms.Textarea(attrs={'class':'form-control mb-2','placeholder':'Tu bio, describete...','rows':5}),
        }