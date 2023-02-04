from django import forms
from .models import Page
from django.contrib.auth.models import User

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title','subtitle','content','author']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'Título'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control','placeholder': 'Subtítulo'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels ={
            'subtitle':'', 'content':'','author':''
        }