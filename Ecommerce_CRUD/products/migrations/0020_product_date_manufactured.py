# Generated by Django 3.1.7 on 2021-05-01 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20210502_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_manufactured',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]