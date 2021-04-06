from django.db import models
from accounts.models import CustomUser

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
    ("18", "RetoPy"),
    ("19", "Other Systems"),

class Post(models.Model):
    text = models.CharField(max_length=500)
    topic = models.CharField(max_length=40)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user_posted = models.ForeignKey(CustomUser on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    platforms = models.CharField(choices= PLATFORM_CHOICES max_length=50)