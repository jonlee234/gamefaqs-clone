from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from post.models import Post


# Create your views here.


class PostCreate(CreateView):
    template_name = "add_post.html"
    model = Post
    fields = ["topic", "game", "platforms", "text", "post_date", "thumbnail"]
