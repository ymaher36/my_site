from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import *


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date']

    def get_queryset(self):
        data = super().get_queryset()[:3]
        return data


class AllPostsView(ListView):
    model = Post
    template_name = 'blog/all-posts.html'
    context_object_name = 'all_posts'
    ordering = ['-date']


class SelectedPostView(DetailView):
    model = Post
    template_name = 'blog/selected-post.html'
