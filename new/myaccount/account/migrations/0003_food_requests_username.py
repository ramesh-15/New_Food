# Generated by Django 4.1.5 on 2023-02-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_remove_food_requests_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="food_requests",
            name="username",
            field=models.CharField(default="", max_length=100),
        ),
    ]
