from django.db import models

# Create your models here.


class Game(models.Model):
    PLATFORM_CHOICES = (
        ("01", "PC"),
        ("02", "PS5"),
        ("03", "XSX"),
        ("04", "Switch"),
        ("05", "iOS"),
        ("06", "Android"),
        ("07", "Arcade"),
        ("08", "PS4"),
        ("09", "PS3"),
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
    title = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField()
    platform = models.CharField(max_length=2, choices=PLATFORM_CHOICES)
    cover_art = models.ImageField(
        upload_to='cover-art/',
        blank=True,
        null=True,
        )

    def __str__(self):
        return f'{self.title} | {self.platform}'
