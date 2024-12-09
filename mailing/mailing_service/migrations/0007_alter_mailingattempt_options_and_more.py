# Generated by Django 5.1.3 on 2024-12-05 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_service", "0006_numattempt"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailingattempt",
            options={"verbose_name": "попытка рассылки", "verbose_name_plural": "попытки рассылки"},
        ),
        migrations.AlterModelOptions(
            name="numattempt",
            options={"verbose_name": "количество рассылок", "verbose_name_plural": "количество рассылок"},
        ),
        migrations.AlterModelTable(
            name="mailingattempt",
            table="mailing_attempt",
        ),
        migrations.AlterModelTable(
            name="numattempt",
            table="num_attempt",
        ),
    ]
