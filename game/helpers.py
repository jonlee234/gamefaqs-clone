import re

from game.models import Game


def searchBy(title):
    game = []
    search = ""

    regex = r"([\s\w\d+]+)"

    find = re.findall(regex, title)

    if find:
        for words in find:
            search = words

    get = Game.objects.all()
    for items in get:
        filter = re.findall(str(search).lower(), str(items).lower())
        if filter:
            print(filter)
            if str(search).lower() in str(items.title).lower():
                id = items.id
                game.append(Game.objects.get(id=id))
            return game
