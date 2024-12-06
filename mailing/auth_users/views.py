from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import CustomUserCreationForm, CustomLoginForm
from .models import CustomUser
from .utils import send_email_for_verify


class RegisterView(CreateView):
    template_name = "auth_users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("auth_users:login_views")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account'
        message = render_to_string('auth_users/verify_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': uid,
            'token': token,
        })
        user.email_user(mail_subject, message, "serega94nn@yandex.ru")

        return super(RegisterView, self).form_valid(form)

        # self.send_welcome_email(user.email, user.password)
        # return super().form_valid(form)


class UserLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "auth_users/login.html"
    success_url = reverse_lazy("mailing_service:home_views")


class ActivateAccount(View):

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect(reverse_lazy('auth_users:login_views'))
        else:
            return HttpResponse('Activation link is invalid')
