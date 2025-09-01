from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import post
from .models import Form
from django.shortcuts import get_object_or_404
from .forms import Arandomform
# Create your views here.

def home(request):
    db_post = post.objects.all()
    if request.method == 'POST':
        form = Arandomform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Form Submitted')
    else:
        form = Arandomform()
    return render(request,'posts/home.html', {'posts': db_post, 'form':form})

def post_page(request, id):
    
    post_dict = get_object_or_404(post,id=id)

    return render(request,'posts/post.html',{'post_dict':post_dict})
