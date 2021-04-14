from django import forms

from .models import Post, Comment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["topic", "game", "platforms", "text", "post_date", "thumbnail"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
