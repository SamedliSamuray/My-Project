# Generated by Django 5.0.7 on 2024-08-01 19:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0019_rename_image_productimage_images"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="main_image",
        ),
    ]
