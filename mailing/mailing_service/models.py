from django.db import models

from auth_users.models import CustomUser


# Create your models here.


class RecipientMailing(models.Model):
    email = models.EmailField(max_length=100, verbose_name="Email")
    full_name = models.CharField(verbose_name="ФИО")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "получатель"
        verbose_name_plural = "получатели"
        db_table = "recipient_mailing"


class Message(models.Model):
    topic_message = models.CharField(verbose_name="Тема письма")
    message = models.TextField(verbose_name="Содержание письма")

    def __str__(self):
        return f"{self.topic_message}"

    class Meta:
        verbose_name = "письмо"
        verbose_name_plural = "письма"
        db_table = "message"


class Mailing(models.Model):
    start_mailing = models.DateTimeField(verbose_name="Дата время начала рассылки")
    end_mailing = models.DateTimeField(verbose_name="Дата время окончания рассылки")
    status = models.CharField(verbose_name="Статус рассылки",
                              choices=(("created", "Создана"), ("Launched", "Запущена"), ("Completed", "Завершена")),
                              default="created")
    messages = models.ForeignKey("Message", on_delete=models.DO_NOTHING, related_name="link_on_message", max_length=100,
                                 verbose_name="Письмо")
    recipients = models.ManyToManyField("RecipientMailing", verbose_name="Получатели", related_name="recipients")

    def __str__(self):
        return f"{self.messages} - {self.recipients}"

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"
        db_table = "mailing"


class MailingAttempt(models.Model):
    datetime_attempt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(verbose_name="Статус рассылки")
    mail_server_response = models.TextField(verbose_name="Ответ почтового сервера")
    mailing = models.ForeignKey(Mailing, on_delete=models.DO_NOTHING, related_name="mailing")

    class Meta:
        verbose_name = "попытка рассылки"
        verbose_name_plural = "попытки рассылки"
        db_table = "mailing_attempt"


class NumAttempt(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_attempt = models.IntegerField(verbose_name="Всего попыток рассылки")
    successful_attempt = models.IntegerField(verbose_name="Успешных попыток рассылки")
    unsuccessful_attempt = models.IntegerField(verbose_name="Неуспешных попыток рассылки")

    class Meta:
        verbose_name = "количество рассылок"
        verbose_name_plural = "количество рассылок"
        db_table = "num_attempt"
