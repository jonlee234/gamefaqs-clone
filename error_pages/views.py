from django.shortcuts import render


def error_404_view(request, exception):
    data = {}
    return render(request, "404.html", data)


def error_500_view(request):
    data = {}
    return render(request, "500.html", data)
