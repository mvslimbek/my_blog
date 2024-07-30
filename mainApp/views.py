from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)

def maqola(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    context = {
        'blog': blog
    }
    return render(request, "maqola.html", context)
