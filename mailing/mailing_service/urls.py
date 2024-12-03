from django.urls import path

from . import views

app_name = "mailing_service"

urlpatterns = [
    path("home_views/", views.HomeView.as_view(), name="home_views"),
    path("form_create_recipient_mailing_views/", views.RecipientCreateView.as_view(),
         name="form_create_recipient_mailing_views"),
    path("form_create_message_views/", views.MessageCreateView.as_view(),
         name="form_create_message_views"),
    path("form_create_mailing_views/", views.MailingCreateView.as_view(),
         name="form_create_mailing_views"),
]
