# Generated by Django 4.2.4 on 2023-09-18 23:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0001_khojuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="GoogleUser",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sub", models.CharField(max_length=200)),
                ("azp", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200)),
                ("given_name", models.CharField(max_length=200)),
                ("family_name", models.CharField(max_length=200)),
                ("picture", models.CharField(max_length=200)),
                ("locale", models.CharField(max_length=200)),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]
