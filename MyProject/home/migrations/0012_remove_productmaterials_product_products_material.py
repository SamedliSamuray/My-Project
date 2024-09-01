# Generated by Django 5.0.7 on 2024-08-23 20:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_productmaterials"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productmaterials",
            name="product",
        ),
        migrations.AddField(
            model_name="products",
            name="material",
            field=models.ManyToManyField(blank=True, to="home.productmaterials"),
        ),
    ]
