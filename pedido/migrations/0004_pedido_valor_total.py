# Generated by Django 3.2.4 on 2021-06-23 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_auto_20210622_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, max_digits=999, null=True),
        ),
    ]