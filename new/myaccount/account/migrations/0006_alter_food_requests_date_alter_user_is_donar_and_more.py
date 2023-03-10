# Generated by Django 4.1.7 on 2023-02-28 07:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_users_donations_flagreq"),
    ]

    operations = [
        migrations.AlterField(
            model_name="food_requests",
            name="date",
            field=models.DateField(default=datetime.date(2023, 2, 28)),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_Donar",
            field=models.BooleanField(default=False, verbose_name="Donar"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_NGO",
            field=models.BooleanField(default=False, verbose_name="NGO"),
        ),
    ]
