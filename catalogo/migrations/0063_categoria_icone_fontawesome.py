# Generated by Django 4.0.2 on 2022-02-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0062_alter_produto_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='icone_fontawesome',
            field=models.CharField(max_length=50, null=True),
        ),
    ]