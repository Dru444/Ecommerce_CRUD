# Generated by Django 3.1.7 on 2021-04-30 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210501_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='media/1.png', upload_to='img/'),
        ),
    ]
