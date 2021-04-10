from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from authentication import views as auth_view
from accounts import views as user_view
from game.views import AddGameView, AllGameView, GameTitleView, PlatformView
from post.views import PostCreate, PostDetailView
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewGames/', AllGameView, name='games'),
    path('viewGames/<int:game_id>/', GameTitleView, name='game-title'),
    path('newGame/', AddGameView, name='add-game'),
    path('viewGames/platform/<int:platform>/', PlatformView, name='platform'),
    path("", user_view.index, name="homepage"),
    path("login/", auth_view.login_view),
    path("signup/", auth_view.signup_view),
    path("logout/", auth_view.logout_view),
    path("post/add/", PostCreate.as_view(), name="post-create"),
    path("posts/<int:pk>", PostDetailView.as_view(), name = "post_detail"),
    # Will change to user_profile_view when I know what content to add.
    path('user/<int:CustomUser_id>/', views.user_profile_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
