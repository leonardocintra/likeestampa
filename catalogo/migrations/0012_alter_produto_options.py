# Generated by Django 3.2 on 2021-05-25 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0011_alter_produto_preco_base'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ('nome',), 'verbose_name': 'produto', 'verbose_name_plural': 'produtos'},
        ),
    ]