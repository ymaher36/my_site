from django.shortcuts import render, get_object_or_404
from .models import *

posts = []


def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def all_posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {
        "all_posts": posts
    })


def selected_post(request, slug):
    wanted_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/selected-post.html', {"post": wanted_post})
