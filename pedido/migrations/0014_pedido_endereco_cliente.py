# Generated by Django 3.2.5 on 2021-07-20 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_auto_20210716_1329'),
        ('pedido', '0013_pedido_pedido_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='endereco_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='usuario.enderecocliente'),
        ),
    ]
