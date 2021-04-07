from django.shortcuts import render
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, "index.html", {"user": user})
