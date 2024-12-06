from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    total_attempt = models.IntegerField(verbose_name="Всего попыток рассылки", default=0)
    successful_attempt = models.IntegerField(verbose_name="Успешных попыток рассылки", default=0)
    unsuccessful_attempt = models.IntegerField(verbose_name="Неуспешных попыток рассылки", default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", ]

    def __str__(self):
        return self.email
