# Generated by Django 4.1.5 on 2023-01-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0008_alter_users_donations_food_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users_donations",
            name="donar_contact",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="users_donations",
            name="pincode",
            field=models.CharField(max_length=6),
        ),
    ]