# Generated by Django 4.1.7 on 2023-02-27 05:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_users_donations_donarmail"),
    ]

    operations = [
        migrations.AddField(
            model_name="users_donations",
            name="donar_name",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AddField(
            model_name="users_donations",
            name="message",
            field=models.TextField(default="", max_length=300),
        ),
        migrations.AddField(
            model_name="users_donations",
            name="ngo_name",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="food_requests",
            name="date",
            field=models.DateField(default=datetime.date(2023, 2, 27)),
        ),
    ]
