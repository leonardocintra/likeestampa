# Generated by Django 3.2.5 on 2021-07-23 01:49

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_remove_cliente_peoplesoft_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=localflavor.br.models.BRCPFField(max_length=14, unique=True, verbose_name='CPF'),
        ),
    ]