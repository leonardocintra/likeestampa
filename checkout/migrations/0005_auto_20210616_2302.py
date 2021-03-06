# Generated by Django 3.2.4 on 2021-06-17 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0022_produtovariacao'),
        ('checkout', '0004_alter_item_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_cor', to='catalogo.produtovariacao'),
        ),
        migrations.AddField(
            model_name='item',
            name='tamanho',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_tamanho', to='catalogo.produtovariacao'),
        ),
    ]
