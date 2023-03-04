from django.shortcuts import render
from .models import *
posts = []


def get_post_date(post):
    return post['date']


def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def all_posts(request):
    return render(request, 'blog/all-posts.html', {"all_posts": posts})


def selected_post(request, slug):
    wanted_post = next(post for post in posts if post['slug'] == slug)
    return render(request, 'blog/selected-post.html', {"post": wanted_post})
