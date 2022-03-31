from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import *


# Create your views here.
def index(request):
    posts = Stack.objects.all()

    context = {
        'title':'Главная страница',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context=context)

def done(request):
    posts = Stack.objects.filter(cat_id=1)

    context ={
        'title':'Изученные технологии',
        'posts': posts,
    }
    return render(request, 'blog/done.html', context=context)

def show_post(request, post_slug):
    post = get_object_or_404(Stack, slug=post_slug)
    return render(request, 'blog/posts.html', {'title':post.title ,'post': post})


def in_process(request):
    posts = Stack.objects.filter(cat_id=2)

    if len(posts) == 0:
        raise Http404()

        
    context ={
        'title':'Изученные технологии',
        'posts': posts,
    }
    return render(request, 'blog/done.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title':'Контакты'})


def PageNotFound(request,exception):
    print(f"{exception}")
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')