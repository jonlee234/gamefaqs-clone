from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from authentication.forms import LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
        if user:
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


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
