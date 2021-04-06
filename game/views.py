from django.shortcuts import render
from game.models import Game

# Create your views here.


def AllGameView(request):
    games = Game.objects.all()
    template = 'all-games.html'
    return render(request, template, {
        'games': games
    })
