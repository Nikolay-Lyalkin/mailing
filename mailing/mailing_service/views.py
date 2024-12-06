from smtplib import SMTPException

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .models import Mailing, RecipientMailing, Message, MailingAttempt

from .forms import RecipientMailingForm, MessageForm, MailingForm


class RecipientListView(ListView):
    model = RecipientMailing
    template_name = "mailing_service/recipients_mailing.html"
    success_url = reverse_lazy("mailing_service:home_views")
    context_object_name = "recipients_mailing"


class RecipientCreateView(CreateView):
    form_class = RecipientMailingForm
    template_name = "mailing_service/form_create_recipient_mailing.html"
    success_url = reverse_lazy("mailing_service:home_views")


class RecipientUpdateView(UpdateView):
    model = RecipientMailing
    form_class = RecipientMailingForm
    template_name = "mailing_service/form_create_recipient_mailing.html"

    def get_success_url(self):
        return reverse_lazy("mailing_service:recipients_mailing_views")


class RecipientDeleteView(DeleteView):
    model = RecipientMailing
    template_name = "mailing_service/delete_recipient.html"
    success_url = reverse_lazy("mailing_service:home_views")
    context_object_name = "recipient"


class RecipientDetailView(DetailView):
    model = RecipientMailing
    template_name = "mailing_service/detail_recipient.html"
    context_object_name = "recipient"
    success_url = reverse_lazy("mailing_service:home_views")


class MessageListView(ListView):
    model = Message
    template_name = "mailing_service/messages.html"
    success_url = reverse_lazy("mailing_service:home_views")
    context_object_name = "messages"


class MessageDetailView(DetailView):
    model = Message
    template_name = "mailing_service/detail_message.html"
    context_object_name = "message"
    success_url = reverse_lazy("mailing_service:home_views")


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = "mailing_service/form_create_message.html"

    def get_success_url(self):
        return reverse_lazy("mailing_service:messages_views")


class MessageDeleteView(DeleteView):
    model = Message
    template_name = "mailing_service/delete_message.html"
    success_url = reverse_lazy("mailing_service:home_views")
    context_object_name = "message"


class MessageCreateView(CreateView):
    form_class = MessageForm
    template_name = "mailing_service/form_create_message.html"
    success_url = reverse_lazy("mailing_service:home_views")


class MailingCreateView(CreateView):
    form_class = MailingForm
    template_name = "mailing_service/form_create_mailing.html"
    success_url = reverse_lazy("mailing_service:home_views")


class MailingDetailView(DetailView):
    model = Mailing
    template_name = "mailing_service/detail_mailing.html"
    context_object_name = "mailing"
    success_url = reverse_lazy("mailing_service:home_views")


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mailing_service/form_create_mailing.html"

    def get_success_url(self):
        return reverse_lazy("mailing_service:mailing_views")


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = "mailing_service/delete_mailing.html"
    success_url = reverse_lazy("mailing_service:mailing_views")
    context_object_name = "mailing"


class SendMailView(View):

    def post(self, request, pk):
        mail = get_object_or_404(Mailing, id=pk)
        user = self.request.user

        try:
            mail_sent = send_mail(mail.messages.topic_message, mail.messages.message, "serega94nn@yandex.ru",
                                  [i.email for i in mail.recipients.all()], fail_silently=False)
            if mail.status != "Запущена":
                mail.status = "Запущена"
                mail.save()
            user.total_attempt += 1

        except SMTPException as e:
            mail_attempt = MailingAttempt(status="Не успешно", mail_server_response=e, mailing=mail)
            user.unsuccessful_attempt += 1
            mail_attempt.save()
            user.save()

        else:
            mail_attempt = MailingAttempt(status="Успешно", mail_server_response="Письмо доставлено", mailing=mail)
            user.successful_attempt += 1
            mail_attempt.save()
            user.save()

        return redirect("mailing_service:home_views")


class MailListView(ListView):
    model = Mailing
    template_name = "mailing_service/mailing.html"
    success_url = reverse_lazy("mailing_service:home_views")
    context_object_name = "mailing"


class MailingListView(ListView):
    model = Mailing
    template_name = "mailing_service/home.html"
    success_url = reverse_lazy("mailing_service:home_views")
    context_object_name = "mailing"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_mailings"] = len(Mailing.objects.all())
        context["total_launched_mailings"] = len(Mailing.objects.filter(status="Запущена"))
        context["total_recipients"] = len(RecipientMailing.objects.all())
        return context


class NotFoundRecipientsView(View):
    template_name = "mailing_service/not_found_recipients.html"
