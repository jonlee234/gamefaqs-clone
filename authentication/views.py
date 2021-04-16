from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from accounts.models import CustomUser, OnlineUsers
from authentication.forms import LoginForm, SignupForm



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data["username"],
                password=data["password"],
            )
        if user:
            users = CustomUser.objects.get(username=user.username)
            users.is_online = True
            users.save()
            login(request, user)
            return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))
    form = LoginForm()
    return render(request, "login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            CustomUser.objects.create_user(
                username=data["username"],
                password=data["password"],
                bio=data["bio"],
                email=data["email"],
                platform_choice_field=data["platform_choice_field"],
                avatar=data.get("avatar"),
            )
            return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))
    form = SignupForm()
    return render(request, "signup.html", {"form": form})


def singup_handler(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/signup/")


@login_required
def logout_view(request):
    users = CustomUser.objects.get(username=request.user)
    users.is_online = False
    users.save()
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
