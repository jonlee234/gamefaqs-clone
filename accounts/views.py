from django.shortcuts import render, HttpResponseRedirect, reverse
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

from accounts.models import CustomUser


@login_required
def index(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, "index.html", {"user": user})


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
