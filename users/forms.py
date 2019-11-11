from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password (Confirm)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario, se creativo'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }
class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario, se creativo'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }