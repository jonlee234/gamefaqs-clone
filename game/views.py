from django.shortcuts import render
from game.models import Game

# Create your views here.


def AllGameView(request):
    template = 'all-games.html'
    games = Game.objects.all()
    return render(request, template, {
        'games': games
    })


def gameTitleView(request, game_id):
    template = 'game-info.html'
    game = Game.objects.get(id=game_id)
    return render(request, template, {
        'game': game
    })
