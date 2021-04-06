from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.CharField(max_length=500)
    topic = models.CharField(max_length=40)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user_posted = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    # platforms = models.ManyToManyField("app.Model", verbose_name=_("")) or models.Charfield w/ choices