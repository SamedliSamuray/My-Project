# Generated by Django 5.0.7 on 2024-07-23 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0013_rename_content_comment_comment_content_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="rating",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
                verbose_name="Rating",
            ),
        ),
    ]