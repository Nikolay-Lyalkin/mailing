from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import CustomUserCreationForm, CustomLoginForm


class RegisterView(CreateView):
    template_name = "auth_users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("mailing_service:home_views")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # self.send_welcome_email(user.email, user.password)
        return super().form_valid(form)


class UserLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "auth_users/login.html"
    success_url = reverse_lazy("mailing_service:home_views")