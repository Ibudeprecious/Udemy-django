from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

posts = [
    {
        "id": 1,
        "title": "Quantum Catalysts",
        "content": "Researchers have developed catalysts that manipulate quantum states of molecules, reducing reaction times from hours to milliseconds."
    },
    {
        "id": 2,
        "title": "Self-Healing Polymers",
        "content": "Next-gen polymers can rebuild broken chemical bonds when exposed to light, making plastics virtually immortal and recyclable forever."
    },
    {
        "id": 3,
        "title": "AI-Driven Reaction design",
        "content": "AI models now predict optimal reaction pathways in real-time, allowing chemists to synthesize complex compounds with zero trial and error."
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
    return render(request,'posts/index.html', {'posts': posts})

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
        return HttpResponseNotFound("<h1> We dont have a post with that id </h1>")

