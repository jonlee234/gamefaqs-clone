from django.shortcuts import render, HttpResponseRedirect, reverse
from accounts.models import CustomUser
from post.models import Post
from game.models import Game
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = CustomUser.objects.get(id=request.user.id)
<<<<<<< HEAD

=======
>>>>>>> d6e1c839c5f3a830124cd30cb60c2adf81869c58
    posts = Post.objects.all().order_by("-post_date")[:10]
    users_list = CustomUser.objects.all().order_by("-date_joined")[:10]
    games = Game.objects.all()
    return render(
        request,
        "index.html",
        {"user": user, "games": games, "posts": posts, "users_list": users_list},
    )


@login_required
def user_profile_view(request, CustomUser_id):
    my_Custom_User = CustomUser.objects.get(id=CustomUser_id)
    return render(request, "user_profile.html", {"user": my_Custom_User})


@login_required
def follower_view(request, user_id):
    request.user.followers.add(CustomUser.objects.get(id=user_id))
    return HttpResponseRedirect(reverse("profile", args=[user_id]))


@login_required
def favorite_game_view(request, game_id):
    request.user.favorite_games.add(Game.objects.get(id=game_id))
    return HttpResponseRedirect(reverse("game-title", args=[game_id]))



@login_required
def unfollow_view(request, user_id):
    request.user.followers.remove(CustomUser.objects.get(id=user_id))
    return HttpResponseRedirect(reverse("profile", args=[user_id]))


@login_required
def unfavorite_game_view(request, game_id):
    request.user.favorite_games.remove(Game.objects.get(id=game_id))
    return HttpResponseRedirect(reverse("game-title", args=[game_id]))


def user_list_view(request):
    user = CustomUser.objects.filter(is_online=True)
    return render(request, 'all-users.html', {
        'user': user
    })


def profile_view(request, username):
    user = CustomUser.objects.get(username=username)
    return render(request, 'user_profile.html', {
        'user': user
    })
