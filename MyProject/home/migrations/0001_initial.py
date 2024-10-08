# Generated by Django 5.0.7 on 2024-08-10 10:09

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("clName", models.CharField(max_length=40)),
                ("color_code", models.CharField(blank=True, max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name="Discounts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=50, unique=True)),
                (
                    "discount_type",
                    models.CharField(
                        choices=[
                            ("percentage", "Percentage"),
                            ("fixed", "Fixed Amount"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "discount_amount",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "max_discount_amount",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Products_Categories",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=60)),
                ("price", models.BigIntegerField()),
                ("descriptions", models.TextField(default=1)),
                (
                    "weight",
                    models.DecimalField(decimal_places=2, default=1.1, max_digits=5),
                ),
                (
                    "width",
                    models.DecimalField(decimal_places=2, default=1.1, max_digits=5),
                ),
                (
                    "height",
                    models.DecimalField(decimal_places=2, default=1.1, max_digits=5),
                ),
                (
                    "depth",
                    models.DecimalField(decimal_places=2, default=1.1, max_digits=5),
                ),
                ("instock", models.BooleanField(default=True)),
                ("materials", models.CharField(default="Wood", max_length=50)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="home.brand",
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="home.color",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="home.products_categories",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("images", models.ImageField(upload_to="product_images/")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="home.products",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                ("price", models.IntegerField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("status", models.BooleanField(default=False)),
                ("delivery", models.IntegerField(blank=True, default=5)),
                (
                    "customers",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "discounts",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.discounts",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order",
                        to="home.products",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment_name", models.CharField(max_length=50, verbose_name="Name:")),
                (
                    "rating",
                    models.IntegerField(
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
                (
                    "comment_email",
                    models.EmailField(max_length=254, verbose_name="E-mail:"),
                ),
                ("comment_content", models.TextField(verbose_name="Content:")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="home.products",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("flat", models.CharField(max_length=50)),
                ("Area", models.CharField(max_length=50)),
                ("pin", models.CharField(max_length=50)),
                ("default_address", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserOrderSummary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "discount_value",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "subtotal",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "total_delivery_cost",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "grand_total",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "phone",
                    models.CharField(blank=True, default="", max_length=50, null=True),
                ),
                (
                    "address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.useraddress",
                    ),
                ),
                (
                    "discounts",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.discounts",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
