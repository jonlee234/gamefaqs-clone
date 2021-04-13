from django.shortcuts import render, HttpResponseRedirect, reverse
from accounts.models import CustomUser
from post.models import Post
from game.models import Game
from django.contrib.auth.decorators import login_required
import random

from accounts.models import CustomUser


@login_required
def index(request):
    user = CustomUser.objects.get(id=request.user.id)
    
    posts = Post.objects.all().order_by("-post_date")[:10]
    users_list= CustomUser.objects.all().order_by("-date_joined")[:10]
    games = Game.objects.all()
    return render(request, "index.html", {"user": user, "games": games, 'posts':posts, "users_list":users_list})
 


@login_required
def follower_view(request, user_id):
    request.user.followers.add(CustomUser.objects.get(id=user_id))
    return render(request, "follow.html")


@login_required
def favorite_game_view(request, game_id):
    request.user.favorite_game.add(CustomUser.objects.get(id=game_id))
    return render(request, "follow.html")


@login_required
def unfollow_view(request, user_id):
    request.user.followers.remove(CustomUser.objects.get(id=user_id))
    return HttpResponseRedirect(reverse("homepage"))


@login_required
def unfavorite_game_view(request, game_id):
    request.user.favorite_game.remove(CustomUser.objects.get(id=game_id))
    return HttpResponseRedirect(reverse("homepage"))


def profile_view(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request, 'profile.html', {
        'user': user
    }) 
