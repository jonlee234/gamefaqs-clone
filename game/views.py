from django.shortcuts import render, HttpResponseRedirect, reverse
from game.models import Game
from game.forms import game_form

# Create your views here.


def AllGameView(request):
    template = 'all-games.html'
    games = Game.objects.all()
    return render(request, template, {
        'games': games
    })


def GameTitleView(request, game_id):
    template = 'game-info.html'
    game = Game.objects.get(id=game_id)
    return render(request, template, {
        'game': game
    })


def AddGameView(request):
    template = 'generic-form.html'
    if request.method == 'POST':
        form = game_form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            game = Game.objects.create(
                title=data['title'],
                description=data['description'],
                platform=data['platform'],
            )
            game.save()
        return HttpResponseRedirect(reverse('game-title', args=[game.id]))

    form = game_form()
    return render(request, template, {
        'form': form
    })
