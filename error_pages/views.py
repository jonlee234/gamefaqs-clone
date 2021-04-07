from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


def error_404_view(request, exception):
    data = {}
    return render(request, "404.html", data)


def error_500_view(request):
    data = {}
    return render(request, "500.html", data)
