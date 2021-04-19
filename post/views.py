from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from post.forms import CommentForm
from post.models import Post, Comment


class PostCreate(LoginRequiredMixin, CreateView):
    template_name = "add_post.html"
    model = Post
    fields = ["topic", "game",  "text",  "thumbnail"]

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
    template_name = "post_list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.author_id = request.user.id
            comment.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "add_comment_to_post.html", {"form": form})
