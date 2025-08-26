from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

posts = articles = [
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
        "title": "AI-Driven Reaction Design",
        "content": "AI models now predict optimal reaction pathways in real-time, allowing chemists to synthesize complex compounds with zero trial and error."
    }
]


def home(request):
    reverse(home)
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
    return HttpResponse(html)

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        html = ''
        html += f''' 
            <h1>{post_dict['id']} - {post_dict['title']}</h1>
            <p>{post_dict['content']}</p>
            <P>Amazing 😍. Coded by Ibude 😉<p>
        
        '''
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("<h1> We dont have a post withh that id </h1>")

def redirect(request, id):
    return HttpResponseRedirect(reverse('post', args=[id]))