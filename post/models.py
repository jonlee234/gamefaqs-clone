from django.db import models
from django.utils import timezone
from django.urls import reverse

from accounts.models import CustomUser
from game.models import Game

# Create your models here.
PLATFORM_CHOICES = (
        ("PC", "PC"),
        ("PS5", "PS5"),
        ("XSX", "XSX"),
        ("Switch", "Switch"),
        ("iOS", "iOS"),
        ("Android", "Android"),
        ("Arcade", "Arcade"),
        ("PS4", "PS4"),
        ("PS3", "PS3"),
        ("Xbox One", "Xbox One"),
        ("Xbox 360", "Xbox 360"),
        ("Sega", "Sega"),
        ("Wii U", "Wii U"),
        ("Wii", "Wii"),
        ("PSP", "PSP"),
        ("Vita", "Vita"),
        ("3DS", "3DS"),
        ("RetoPy", "RetoPy"),
        ("Other Systems", "Other Systems"),
    )


class Post(models.Model):
    text = models.TextField(max_length=1000)
    post_date = models.DateField(default=timezone.now)
    topic = models.CharField(max_length=40)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user_posted = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="media/", default = "static/assets/images/hs.jpeg")
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
