from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from .forms import RecipientMailingForm, MessageForm, MailingForm


class HomeView(TemplateView):
    template_name = "mailing_service/home.html"

class RecipientCreateView(CreateView):
    form_class = RecipientMailingForm
    template_name = "mailing_service/form_create_recipient_mailing.html"
    success_url = reverse_lazy("mailing_service:home_views")


class MessageCreateView(CreateView):
    form_class = MessageForm
    template_name = "mailing_service/form_create_message.html"
    success_url = reverse_lazy("mailing_service:home_views")


class MailingCreateView(CreateView):
    form_class = MailingForm
    template_name = "mailing_service/form_create_mailing.html"
    success_url = reverse_lazy("mailing_service:home_views")