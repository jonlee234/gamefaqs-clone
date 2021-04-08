from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from game.models import Game
from game.forms import game_form, SearchBar
import re

# Create your views here.


class AllGameView(View):
    def get(self, request):
        template = 'all-games.html'

        search_bar = SearchBar()

        games = Game.objects.all()
        return render(request, template, {
            'games': games,
            'search': search_bar
        })

    def post(self, request):
        search_bar = SearchBar(request.POST)
        title = ''
        platform = ''

        if search_bar.is_valid():
            data = search_bar.cleaned_data

            title = data['search']
            platform = data['search_by']

            return HttpResponseRedirect('/')


def GameTitleView(request, game_id):
    template = 'game-info.html'
    game = Game.objects.get(id=game_id)
    return render(request, template, {
        'game': game
    })


class AddGameView(LoginRequiredMixin, View):
    def get(self, request):
        template = 'generic-form.html'
        form = game_form()
        return render(request, template, {
            'form': form
        })

    def post(self, request):
        form = game_form(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            game = Game.objects.create(
                title=data['title'],
                description=data['description'],
                platform=data['platform'],
                cover_art=data['cover_art']
            )
            game.save()
        return HttpResponseRedirect(reverse('game-title', args=[game.id]))


def PlatformView(request, platform):
    template = 'platform.html'
    string = str(platform)

    if len(string) < 2:
        string = '0' + str(platform)

    games = Game.objects.filter(platform=string)
    return render(request, template, {
        'games': games
    })


def search(request):
    
    filter = Game.objects.all().filter(platform=str(search_by))
            for items in filter:
                if str(search).lower() in str(items.title).lower():
                    title = str(search).lower())