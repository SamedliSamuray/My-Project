# Generated by Django 5.0.7 on 2024-08-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userordersummary",
            name="phone",
        ),
        migrations.AddField(
            model_name="useraddress",
            name="phone",
            field=models.CharField(blank=True, default="", max_length=50, null=True),
        ),
    ]
