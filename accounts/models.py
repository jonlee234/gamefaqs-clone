from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

PLATFORM_CHOICES = (
    ("1", "PC"),
    ("2", "PlayStation"),
    ("3", "Xbox"),
    ("4", "Nintendo"),
    ("5", "Arcade"),
    ("6", "Sega"),
)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(_("abc@blah.com"), unique=True)
    bio = models.CharField(max_length=500)
    date_joined = models.DateField(default=datetime.timezone.now)
    platform_choice_field = form.MultipleChoiceField(choices=PLATFORM_CHOICES)
    avatar = models.ImageField()

    # update to anything else you'd like to show here
    def __str__(self):
        return self.username


# Profile Pic(null)
