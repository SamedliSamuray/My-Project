# Generated by Django 5.0.7 on 2024-08-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0008_alter_payments_payment_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="transaction_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
