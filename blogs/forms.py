from django import forms
from .models import Blog
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','subtitle','content','picture',]
        labels = {
            'title': '',
            'subtitle': '',
            'content': '',
            'picture': '',
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Titulo del post'}),
            'subtitle':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Subtitulo del post'}),
            'content':forms.Textarea(attrs={'class':'form-control mb-2','placeholder':'Contenido...  ','rows':5}),
            'picture':forms.FileInput(attrs={'class':'w-100'}),
        }