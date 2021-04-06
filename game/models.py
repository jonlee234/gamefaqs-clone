from django.db import models

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField()
    platform = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title} | {self.platform}'
