from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "auth_users"

urlpatterns = [
    path("register_views/", views.RegisterView.as_view(), name="register_views"),
    path("login_views/", views.UserLoginView.as_view(), name="login_views"),
    path("logout_views/", LogoutView.as_view(next_page="mailing_service:home_views"), name="logout_views"),
    path("activate_views/<uidb64>/<token>/", views.ActivateAccount.as_view(), name='activate_views'),
]
