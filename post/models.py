from django.db import models
from django.utils import timezone
from django.urls import reverse

from accounts.models import CustomUser
from game.models import Game

# Create your models here.
PLATFORM_CHOICES = (
    ("1", "PC"),
    ("2", "PS5"),
    ("3", "XSX"),
    ("4", "Switch"),
    ("5", "iOS"),
    ("6", "Android"),
    ("7", "Arcade"),
    ("8", "PS4"),
    ("9", "PS3"),
    ("10", "Xbox One"),
    ("11", "Xbox 360"),
    ("12", "Sega"),
    ("13", "Wii U"),
    ("14", "Wii"),
    ("15", "PSP"),
    ("16", "Vita"),
    ("17", "3DS"),
    ("18", "RetroPy"),
    ("19", "Other Systems"),
)


class Post(models.Model):
    text = models.TextField(max_length=1000)
    post_date = models.DateTimeField(default=timezone.now)
    topic = models.CharField(max_length=40)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user_posted = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="media/")
    platforms = models.CharField(choices=PLATFORM_CHOICES, max_length=50)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    class Meta:
        ordering = ["-created_date"]

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, max_length=1200, related_name="comments"
    )
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
