from django.db import models


class Game(models.Model):
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
    title = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField()
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    cover_art = models.ImageField(
        upload_to="cover-art/",
        blank=True,
        null=True,
        default="cover-art/cover-art-default.png",
    )

    def __str__(self):
        return f"{self.title} | {self.platform}"
