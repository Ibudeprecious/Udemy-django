from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import registerform, loginform
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method == 'POST':
            form = registerform(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                return HttpResponseRedirect(reverse('home'))
        else:
            form = registerform()

    return render(request,'account/register.html',{'form':form})

def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method == 'POST':
            form = loginform(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse('home'))
        else:
            form = loginform()
    return render(request,'account/login.html',{'form':form})

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
