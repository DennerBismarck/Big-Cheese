# Generated by Django 5.0.1 on 2024-02-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos_das_vendas',
            name='pdv_PrecoTotalItem',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Valor total do produto'),
        ),
        migrations.AlterField(
            model_name='produtos_das_vendas',
            name='pdv_qtd',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade comprada'),
        ),
    ]