# Generated by Django 5.1.3 on 2024-12-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_users", "0005_customuser_token"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResetPassword",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
