# Generated by Django 5.0.7 on 2024-09-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0019_alter_comment_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="image",
            field=models.ImageField(
                blank=True, default="/media/profil_picture/unnamed.jpg", upload_to=""
            ),
        ),
    ]
