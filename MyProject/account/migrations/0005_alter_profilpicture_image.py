# Generated by Django 5.0.7 on 2024-09-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0004_rename_address_profilpicture_user_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilpicture",
            name="image",
            field=models.ImageField(
                blank=True,
                default="profil_picture/unnamed.jpg",
                upload_to="profil_picture",
            ),
        ),
    ]
