# Generated by Django 3.2.5 on 2021-08-05 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0043_auto_20210804_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeloproduto',
            name='descricao_cliente',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
