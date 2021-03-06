# Generated by Django 3.2.4 on 2021-06-24 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0024_produtovariacao_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeloProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Descricao')),
                ('medidas', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Modificado em')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelo_produto', to='catalogo.produto')),
            ],
            options={
                'verbose_name': 'Modelos',
                'verbose_name_plural': 'Modelos',
                'db_table': 'modelo_produto',
                'ordering': ('nome',),
            },
        ),
    ]
