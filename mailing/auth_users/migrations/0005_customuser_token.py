# Generated by Django 5.1.3 on 2024-12-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_users", "0004_alter_customuser_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="token",
            field=models.CharField(default=1, unique=True),
            preserve_default=False,
        ),
    ]