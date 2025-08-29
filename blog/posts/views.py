from django.shortcuts import render
from django.http import Http404
from .models import post
from django.shortcuts import get_object_or_404
# Create your views here.

all_posts = [
    {
        "title": "Accountability in Reading",
        "content": "Keeping track of the books you’ve committed to read ensures growth and discipline. Accountability partners can help you stay consistent and finish what you start."
    },
    {
        "title": "Accountability in Skill Development",
        "content": "Learning a skill requires practice and feedback. By sharing progress with a mentor or group, you create accountability that drives you to keep improving."
    },
    {
        "title": "Accountability in Time Management",
        "content": "Time is a resource you can’t recover once lost. Using schedules, deadlines, or accountability buddies helps prevent procrastination and keeps you focused."
    },
    {
        "title": "Accountability in Financial Management",
        "content": "Tracking income, expenses, and savings with transparency creates financial discipline. Accountability ensures you avoid waste and make wiser money decisions."
    }
]

def home(request):
    db_post = post.objects.all()
    return render(request,'posts/home.html', {'posts': db_post})

def post_page(request, id):
    
    post_dict = get_object_or_404(post,id=id)

    return render(request,'posts/post.html',{'post_dict':post_dict})
