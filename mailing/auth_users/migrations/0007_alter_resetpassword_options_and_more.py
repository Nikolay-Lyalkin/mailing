# Generated by Django 5.1.3 on 2024-12-07 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auth_users", "0006_resetpassword"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="resetpassword",
            options={"verbose_name": "сброс пароля", "verbose_name_plural": "сброс паролей"},
        ),
        migrations.AlterModelTable(
            name="resetpassword",
            table="reset_password",
        ),
    ]
