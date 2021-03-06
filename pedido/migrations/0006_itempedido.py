# Generated by Django 3.2.4 on 2021-07-01 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0031_alter_modelovariacao_options'),
        ('pedido', '0005_auto_20210627_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_pedido_cor', to='catalogo.modelovariacao')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_pedido_modelo', to='catalogo.modeloproduto')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido_item', to='pedido.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogo.produto')),
                ('tamanho', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_pedido_tamanho', to='catalogo.modelovariacao')),
            ],
            options={
                'verbose_name': 'Item do pedido',
                'verbose_name_plural': 'Itens dos pedidos',
                'db_table': 'item_pedido',
            },
        ),
    ]

    run_before = [
        ('catalogo', '0055_auto_20210910_1354'),
    ]
