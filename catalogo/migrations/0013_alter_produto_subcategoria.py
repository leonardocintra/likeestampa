# Generated by Django 3.2.3 on 2021-05-26 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0012_alter_produto_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='subcategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto_subcategoria', to='catalogo.subcategoria'),
        ),
    ]
