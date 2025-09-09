from django.urls import path
from .views import login_view, logout_view, register_view, RegisterView, LoginView, LogoutView, TokenRefreshViewCustom

urlpatterns = [
    # Frontend login/logout/register
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),  # <-- frontend HTML form

    # API endpoints
    path("api/register/", RegisterView.as_view(), name="api-register"),  # <-- API
    path("api-login/", LoginView.as_view(), name="api-login"),
    path("api-logout/", LogoutView.as_view(), name="api-logout"),
    path("refresh/", TokenRefreshViewCustom.as_view(), name="token-refresh"),
]
