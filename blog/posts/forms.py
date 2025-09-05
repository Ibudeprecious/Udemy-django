from django import forms
from .models import comment
from django.core import validators

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control'})
        }