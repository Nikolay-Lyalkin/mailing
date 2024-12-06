# Generated by Django 5.1.3 on 2024-12-06 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_service", "0007_alter_mailingattempt_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(default="Создана", verbose_name="Статус рассылки"),
        ),
        migrations.AlterField(
            model_name="mailingattempt",
            name="mailing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="mailing", to="mailing_service.mailing"
            ),
        ),
    ]
