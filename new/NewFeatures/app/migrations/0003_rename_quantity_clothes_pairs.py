# Generated by Django 4.1.7 on 2023-03-07 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_clothes_delete_food_requests"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clothes",
            old_name="quantity",
            new_name="pairs",
        ),
    ]