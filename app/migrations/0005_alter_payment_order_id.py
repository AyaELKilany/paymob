# Generated by Django 3.2.7 on 2022-11-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_payment_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_id',
            field=models.BigIntegerField(default=None),
        ),
    ]
