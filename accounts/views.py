from django.shortcuts import render
from accounts.models import CustomUser
from post.models import Post
from game.models import Game
from django.contrib.auth.decorators import login_required
import random

# Create your views here.


@login_required
def index(request):
    user = CustomUser.objects.get(id=request.user.id)
    posts = Post.objects.all().order_by("-post_date")[:10]
    users_list= CustomUser.objects.all().order_by("-date_joined")[:10]
    games = Game.objects.all()
    return render(request, "index.html", {"user": user, "games": games, 'posts':posts, "users_list":users_list})
