# Generated by Django 4.1.7 on 2023-04-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_donaruser_confirm_password_donaruser_new_password"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoginDetials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
                ("login_data", models.DateTimeField(auto_now_add=True)),
                ("logout_data", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
