# Generated by Django 3.2.4 on 2021-06-24 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0027_alter_modeloproduto_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeloproduto',
            name='medidas',
        ),
        migrations.AddField(
            model_name='produtovariacao',
            name='outras_informacoes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='ProdutoImagem',
        ),
    ]