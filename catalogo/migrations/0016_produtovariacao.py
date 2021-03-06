# Generated by Django 3.2.3 on 2021-06-05 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0015_variacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoVariacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Modificado em')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto_variacao', to='catalogo.produto')),
                ('variacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='variacao_produto', to='catalogo.variacao')),
            ],
            options={
                'verbose_name': 'Variação do produto',
                'verbose_name_plural': 'Variações do produto',
                'db_table': 'produto_variacao',
                'ordering': ('-created_at',),
            },
        ),
    ]
