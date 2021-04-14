from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from game.models import Game
from game.forms import game_form, SearchBar
from game.helpers import searchBy


class AllGameView(View):
    def get(self, request):
        template = "all-games.html"

        search_bar = SearchBar()

        games = Game.objects.all()
        return render(request, template, {"games": games, "search": search_bar})

    def post(self, request):
        search_bar = SearchBar(request.POST)
        title = ""

        if search_bar.is_valid():
            data = search_bar.cleaned_data

            title = data["search"]

            return HttpResponseRedirect(reverse("search", args=[title]))


def GameTitleView(request, game_id):
    template = "game-info.html"
    game = Game.objects.get(id=game_id)
    return render(request, template, {"game": game})


class AddGameView(LoginRequiredMixin, View):
    def get(self, request):
        template = "generic-form.html"
        form = game_form()
        return render(request, template, {"form": form})

    def post(self, request):
        form = game_form(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            if data["cover_art"]:
                game = Game.objects.create(
                    title=data["title"],
                    description=data["description"],
                    platform=data["platform"],
                    cover_art=data["cover_art"],
                )
                game.save()
                return HttpResponseRedirect(reverse("game-title", args=[game.id]))
            else:
                game = Game.objects.create(
                    title=data["title"],
                    description=data["description"],
                    platform=data["platform"],
                )
                game.save()
                return HttpResponseRedirect(reverse("game-title", args=[game.id]))


def PlatformView(request, platform):
    template = "platform.html"
    string = str(platform)

    if len(string) < 2:
        string = "0" + str(platform)

    games = Game.objects.filter(platform=string)
    return render(request, template, {"games": games})


def Search(request, title):
    template = "search.html"
    games = searchBy(title)

    return render(request, template, {"games": games})
