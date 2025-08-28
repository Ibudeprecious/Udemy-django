from django.shortcuts import render
from django.http import Http404


# Create your views here.

posts = [
    {
        "id": 1,
        "title": "Accountability in Reading",
        "content": "Keeping track of the books you’ve committed to read ensures growth and discipline. Accountability partners can help you stay consistent and finish what you start."
    },
    {
        "id": 2,
        "title": "Accountability in Skill Development",
        "content": "Learning a skill requires practice and feedback. By sharing progress with a mentor or group, you create accountability that drives you to keep improving."
    },
    {
        "id": 3,
        "title": "Accountability in Time Management",
        "content": "Time is a resource you can’t recover once lost. Using schedules, deadlines, or accountability buddies helps prevent procrastination and keeps you focused."
    },
    {
        "id": 4,
        "title": "Accountability in Financial Management",
        "content": "Tracking income, expenses, and savings with transparency creates financial discipline. Accountability ensures you avoid waste and make wiser money decisions."
    }
]

# posts = []

def home(request):
    html = ''
    for post in posts:
        html += f'''
        <div>
        <a href="/post/{post['id']}/">
            <h1>{post['id']} - {post['title']}</h1> </a>
            <p>{post['content']}</p>
        </div>
        
        '''
    html += "<h1> Proudly coded by Ibude 😉 </h1>"
    return render(request,'posts/home.html', {'posts': posts})

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        return render(request,'posts/post.html',{'post_dict':post_dict})
    else:
        raise Http404()

