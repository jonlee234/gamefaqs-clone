from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from game.models import Game

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


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    bio = models.CharField(max_length=500)
    date_joined = models.DateField(default=timezone.now)
    platform_choice_field = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    avatar = models.ImageField(null=True, blank=True, upload_to="media/", default='media/default.png')
    followers = models.ManyToManyField("self", symmetrical=False)
    favorite_games = models.ManyToManyField(Game, symmetrical=False)
    is_online = models.BooleanField(default=False)
    def __str__(self):
        return self.username


class OnlineUsers(models.Model):
    user_list = models.ManyToManyField(CustomUser, symmetrical=False)

