# Generated by Django 4.0.5 on 2022-06-14 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0069_modelo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]