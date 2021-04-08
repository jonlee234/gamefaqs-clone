"""gamefaqs_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import handler404, handler500

from authentication import views as auth_view
from accounts import views as user_view
from game.views import AddGameView, AllGameView, GameTitleView, PlatformView, Search
from post import views as post_view
from error_pages.views import error_404_view, error_500_view


from post.views import PostCreate, PostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewGames/', AllGameView.as_view(), name='games'),
    path('viewGames/<int:game_id>/', GameTitleView, name='game-title'),
    path('newGame/', AddGameView.as_view(), name='add-game'),
    path('viewGames/platform/<int:platform>/', PlatformView, name='platform'),
    path("", user_view.index, name="homepage"),
    path("login/", auth_view.login_view),
    path("signup/", auth_view.signup_view),
    path("logout/", auth_view.logout_view),
    path('viewGames/search/<str:title>/', Search, name='search'),
    path("post/add/", PostCreate.as_view(), name="post-create"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'error_pages.views.error_404_view'
handler500 = 'error_pages.views.error_500_view'
