from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Никнейм",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 400px"}),
    )
    email = forms.EmailField(
        label="Электронная почта", widget=forms.EmailInput(attrs={"class": "form-control", "style": "width: 400px"})
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "style": "width: 400px"})
    )
    password2 = forms.CharField(
        label="Повторите пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "style": "width: 400px"})
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Электронная почта", widget=forms.EmailInput(attrs={"class": "form-control", "style": "width: 400px"})
    )
    password = forms.CharField(
        label="Повторите пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "style": "width: 400px"})
    )

    class Meta:
        model = CustomUser
        fields = ("email", "password")
