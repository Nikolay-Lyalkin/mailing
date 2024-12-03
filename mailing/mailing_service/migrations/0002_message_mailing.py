# Generated by Django 5.1.3 on 2024-12-03 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_service", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("topic_message", models.CharField(verbose_name="Тема письма")),
                ("message", models.TextField(verbose_name="Содержание письма")),
            ],
            options={
                "verbose_name": "письмо",
                "verbose_name_plural": "письма",
                "db_table": "message",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("start_mailing", models.DateTimeField(verbose_name="Дата время начала рассылки")),
                ("end_mailing", models.DateTimeField(verbose_name="Дата время окончания рассылки")),
                (
                    "recipients",
                    models.ManyToManyField(to="mailing_service.recipientmailing", verbose_name="Получатели"),
                ),
                (
                    "messages",
                    models.ForeignKey(
                        max_length=100,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="link_on_message",
                        to="mailing_service.message",
                        verbose_name="Письмо",
                    ),
                ),
            ],
            options={
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
                "db_table": "mailing",
            },
        ),
    ]