# Generated by Django 3.1.7 on 2021-05-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20210501_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('MOBILE PHONE', 'MOBILE PHONE'), ('CLOTHING', 'CLOTHING'), ('LAPTOP', 'LAPTOP'), ('FOOD', 'FOOD')], max_length=100),
        ),
    ]
