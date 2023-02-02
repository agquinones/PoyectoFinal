from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title','subtitle','content']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'Título'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control','placeholder': 'Subtítulo'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels ={
            'title':'', 'subtitle':'', 'content':''
        }