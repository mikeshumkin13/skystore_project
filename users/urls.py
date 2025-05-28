from django.urls import path
from .views import UserRegisterView, ProfileView
from django.contrib.auth.views import LoginView, LogoutView

app_name = "users"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:home"), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
