# Generated by Django 3.2.5 on 2021-10-13 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0058_tamanhomodelo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tamanhomodelo',
            options={'ordering': ('created_at',), 'verbose_name': 'Tamanhos e Modelos', 'verbose_name_plural': 'Tamanhos e Modelos'},
        ),
        migrations.AddField(
            model_name='tamanho',
            name='descricao_cliente',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
