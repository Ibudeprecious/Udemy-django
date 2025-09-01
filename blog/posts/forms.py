from django import forms
from .models import Form
from django.core import validators

def start_s(value):
    if value[0] !='s' and value[0] !='S':
        raise forms.ValidationError('This field should start with S')
        
class Arandomform(forms.ModelForm):
    name = forms.CharField(help_text='Please put in the right email address',label='Your name:',validators=[validators.MinLengthValidator(10),start_s], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Whats your name?'}))
    email = forms.EmailField(label='Your Email:',validators=[start_s], widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Whats your email address?'}))
    class Meta:
        model = Form
        fields = '__all__' #or ['name', 'email', 'phone_number', 'about']
        # exclude = ['email']
        labels = {
            'phone_number':'Your Phone Number',
            'about':'Your Bio'
        } 
        widgets = {
            'phone_number': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Whats your phone number?'}),
            'about': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Tell us about yourself'})
        }
       
        
        