from django import forms
from django.forms import ModelForm

from myapp.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
        }
