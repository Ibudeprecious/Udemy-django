from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class registerform(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your username here'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email here'}))
    first_name = forms.CharField(label='First Name', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your First Name Here'}))
    last_name = forms.CharField(label='Last Name', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Last name here'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Your password here'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password here'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class loginform(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your username here'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Your password here'}))

