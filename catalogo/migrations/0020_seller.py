# Generated by Django 3.2.4 on 2021-06-14 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0019_alter_produtovariacao_tipo_variacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('site', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Seller',
                'verbose_name_plural': 'Seller',
                'db_table': 'seller',
                'ordering': ('nome',),
            },
        ),
    ]