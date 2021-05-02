# Generated by Django 3.1.7 on 2021-04-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210430_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offers',
            field=models.CharField(blank=True, choices=[('0', 'NO OFFER'), ('1', '10% OFF WITH CREDIT CARDS'), ('2', 'RS.100 CASHBACK'), ('3', 'FREE SHIPPING')], max_length=200),
        ),
    ]
