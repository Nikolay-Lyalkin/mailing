from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "auth_users"

urlpatterns = [
    path("register_views/", views.RegisterView.as_view(), name="register_views"),
    path("login_views/", views.UserLoginView.as_view(), name="login_views"),
    path("logout_views/", LogoutView.as_view(next_page="mailing_service:home_views"), name="logout_views"),
    path("confirm_email_views/", TemplateView.as_view(template_name="auth_users/confirm_email.html"),
         name="confirm_email_views"),
    path("verify_email_views/", views.EmailVerify.as_view(), name="verify_email_views"),
]
