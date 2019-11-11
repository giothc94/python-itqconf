from django import forms
from .models import ContactSpeaker

class ContactSpeakerForm(forms.ModelForm):
    class Meta:
        model = ContactSpeaker
        fields = ['first_name','last_name','job_title','email','message']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}),
            'job_title':forms.TextInput(attrs={'class':'form-control','placeholder':'Tu experticia, titulo.'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholder':'Sobre que quieres hablar...','rows':5})
        }
        
    


