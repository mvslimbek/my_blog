from collections import defaultdict

from django.shortcuts import render
from .models import *
MONTH_TRANSLATIONS = {
    'january': 'Yanvar',
    'february': 'Fevral',
    'march': 'Mart',
    'april': 'Aprel',
    'may': 'May',
    'june': 'Iyun',
    'july': 'Iyul',
    'august': 'Avgust',
    'september': 'Sentabr',
    'october': 'Oktabr',
    'november': 'Noyabr',
    'december': 'Dekabr'
}


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def maqola(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    context = {
        'blog': blog
    }
    return render(request, "maqola.html", context)


def blog(request):
    blogs = BlogPost.objects.all()

    blog_dict = defaultdict(lambda: defaultdict(list))
    for blog in blogs:
        year = blog.datetime.year
        month = blog.datetime.strftime('%B').lower()
        uzbek_month = MONTH_TRANSLATIONS[month]
        blog_dict[year][uzbek_month].append(blog)

    blog_dict = {year: dict(months) for year, months in blog_dict.items()}

    context = {
        'blogs': blog_dict
    }
    return render(request, 'blog.html', context)


def talksview(request):
    talks = Talks.objects.all()
    context={
        'talks':talks
    }
    return render(request, "talks.html", context)
