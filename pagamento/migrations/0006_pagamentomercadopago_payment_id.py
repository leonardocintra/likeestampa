# Generated by Django 3.2.4 on 2021-06-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0005_alter_pagamentomercadopago_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamentomercadopago',
            name='payment_id',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
