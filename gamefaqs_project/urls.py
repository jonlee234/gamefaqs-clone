from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import handler404, handler500

from authentication import views as auth_view
from accounts import views as user_view
from game.views import AddGameView, AllGameView, GameTitleView, PlatformView, Search
from error_pages.views import error_404_view, error_500_view
from accounts.views import (
    favorite_game_view,
    follower_view,
    unfavorite_game_view,
    unfollow_view,
    user_profile_view,
)

from post.views import PostCreate, PostDetailView, PostListView
from accounts.views import favorite_game_view


urlpatterns = [
    path("", user_view.index, name="homepage"),
    path("viewGames/", AllGameView.as_view(), name="games"),
    path("viewGames/<int:game_id>/", GameTitleView, name="game-title"),
    path("newGame/", AddGameView.as_view(), name="add-game"),
    path("viewGames/platform/<int:platform>/", PlatformView, name="platform"),
    path("login/", auth_view.login_view),
    path("signup/", auth_view.signup_view),
    path("logout/", auth_view.logout_view),
    path("viewGames/search/<str:title>/", Search, name="search"),
    path("post/add/", PostCreate.as_view(), name="post-create"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("admin/", admin.site.urls),
    path("follow/<int:user_id>", follower_view),
    path("unfollow/<int:user_id>", unfollow_view),
    path("user/<int:CustomUser_id>/", user_profile_view),
    path("favorite_game/<int:game_id>", favorite_game_view),
    path("unfavorite_game/<int:game_id>", unfavorite_game_view),
    path("posts/", PostListView.as_view(), name="post-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "error_pages.views.error_404_view"
handler500 = "error_pages.views.error_500_view"
