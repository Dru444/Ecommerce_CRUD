# Generated by Django 3.1.7 on 2021-05-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20210501_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offers',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
