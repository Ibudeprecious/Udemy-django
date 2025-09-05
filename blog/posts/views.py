from django.shortcuts import render
from .models import post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import commentform
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    db_post = post.objects.all().order_by('-id')
    paginator = Paginator(db_post,4) #show 4 posts per page
    current_page = paginator.get_page(request.GET.get('p',2))
    return render(request,'posts/home.html', {'posts': current_page})

def post_page(request, id):
    
    post_dict = get_object_or_404(post,id=id)
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post_dict
            comment.save()
            posturl = reverse(post_page,args=[id])
            return HttpResponsePermanentRedirect(posturl)
    else:
        form = commentform()

    return render(request,'posts/post.html',{'post_dict':post_dict,'comment_form':form})
