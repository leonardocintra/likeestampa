# Generated by Django 3.2.5 on 2021-07-23 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0038_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeloproduto',
            name='modelo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='catalogo.modelo'),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='descricao',
            field=models.CharField(default='T-Shirt', max_length=50),
        ),
    ]
