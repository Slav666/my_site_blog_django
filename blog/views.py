from django.db.models import query
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.


class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ["-date"]


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
