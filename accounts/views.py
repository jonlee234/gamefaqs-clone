from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import CustomUser


@login_required
def index(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, "index.html", {"user": user})


def user_profile_view(request, CustomUser_id):
    my_Custom_User = CustomUser.objects.get(id=CustomUser_id)
    return render(
        request, "user_profile.html", {"user": my_Custom_User}
    )
