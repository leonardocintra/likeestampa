# Generated by Django 3.2.4 on 2021-06-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20210617_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='referencia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='telefone_contato',
            field=models.CharField(default='11996226771', max_length=12),
        ),
    ]
