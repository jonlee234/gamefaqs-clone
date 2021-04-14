from django import forms
from .models import Post, Comment


# text = models.CharField(max_length=500)
#     post_date = models.DateTimeField(default=timezone.now)
#     topic = models.CharField(max_length=40)
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     user_posted = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     thumbnail = models.ImageField(null=True, blank=True, upload_to="images/")
#     platforms = models.CharField(choices=PLATFORM_CHOICES, max_length=50)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["topic", "game", "platforms", "text", "post_date", "thumbnail"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
