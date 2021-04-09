from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from post.models import Post


# Create your views here.


class PostCreate(CreateView):
    template_name = "add_post.html"
    model = Post
    fields = ["topic", "game", "platforms", "text", "post_date", "thumbnail"]

    def form_valid(self, form):
        form.instance.user_posted = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class PostListView(ListView):

    model = Post
    paginate_by = 10  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context