# Generated by Django 5.0.7 on 2024-08-10 14:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_remove_userordersummary_phone_useraddress_phone"),
    ]

    operations = [
        migrations.RenameField(
            model_name="useraddress",
            old_name="Area",
            new_name="area",
        ),
    ]
