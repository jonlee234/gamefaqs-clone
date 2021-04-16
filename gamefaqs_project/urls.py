from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

from authentication import views as auth_view
from accounts import views as user_view
from accounts.views import (
    favorite_game_view,
    follower_view,
    unfavorite_game_view,
    unfollow_view,
    user_profile_view,
    favorite_game_view,
    user_list_view,
)
from game.views import (
    AddGameView,
    AllGameView,
    GameTitleView,
    PlatformView,
    Search,
)
from error_pages.views import (
    error_404_view,
    error_500_view,
)
from post.views import (
    PostCreate,
    PostDetailView,
    PostListView,
    add_comment_to_post,
)


urlpatterns = [
    # Core links
    path("", user_view.index, name="homepage"),
    path("admin/", admin.site.urls, name="admin"),
    # Game Related Links
    path("viewGames/", AllGameView.as_view(), name="games"),
    path("viewGames/<int:game_id>/", GameTitleView, name="game-title"),
    path("newGame/", AddGameView.as_view(), name="add-game"),
    path("viewGames/platform/<int:platform>/", PlatformView, name="platform"),
    path("viewGames/search/<str:title>/", Search, name="search"),
    # Auth Links
    path("login/", auth_view.login_view, name="login"),
    path("signup/", auth_view.signup_view, name="signup"),
    path("logout/", auth_view.logout_view, name="logout"),
    # Post Links
    path("post/add/", PostCreate.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/comment/", add_comment_to_post, name="add_comment_to_post"),
    # Follow Links
    path("follow/<int:user_id>", follower_view, name="follow"),
    path("unfollow/<int:user_id>", unfollow_view, name="unfollow"),
    # User/Profile Links
    path("user/<int:CustomUser_id>/", user_profile_view, name="user-profile"),
    # path("viewProfile/<str:username>/", user_profile_view, name="profile"),
    path("viewUsers/", user_list_view, name="users"),
    # Favorites
    path("favorite_game/<int:game_id>", favorite_game_view, name="favorite_game"),
    path("unfavorite_game/<int:game_id>", unfavorite_game_view, name="unfavorite_game"),
    # Statics
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TODO Add other errors
handler404 = "error_pages.views.error_404_view"
handler500 = "error_pages.views.error_500_view"
