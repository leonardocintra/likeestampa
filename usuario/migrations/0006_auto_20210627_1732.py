# Generated by Django 3.2.4 on 2021-06-27 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_alter_cliente_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em'),
        ),
    ]
