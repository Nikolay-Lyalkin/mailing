

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import request

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import CustomUserCreationForm, CustomLoginForm
from .utils import send_email_for_verify


class RegisterView(CreateView):
    template_name = "auth_users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("mailing_service:home_views")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        send_email_for_verify(request, user)
        return redirect("auth_users:confirm_email_views")
        # self.send_welcome_email(user.email, user.password)
        # return super().form_valid(form)


class UserLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "auth_users/login.html"
    success_url = reverse_lazy("mailing_service:home_views")


class EmailVerify(View):
    pass