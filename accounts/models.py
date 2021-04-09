from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from game.models import Game

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
    ("18", "RetoPy"),
    ("19", "Other Systems"),
)

"""
notes:
needed to change username to unique
fix the emailfield to only unique true and max length
datetime should refer to current datetime per timezone now
Choice Field needs to be models.Charfield
"""


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    bio = models.CharField(max_length=500)
    date_joined = models.DateField(default=timezone.now)
    platform_choice_field = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    avatar = models.ImageField(null=True, blank=True, upload_to="media/")
    followers = models.ManyToManyField('self', symmetrical=False)
    favorite_games = models.ManyToManyField(Game, symmetrical=False)
    # update to anything else you'd like to show here
    def __str__(self):
        return self.username


# Profile Pic(null)
