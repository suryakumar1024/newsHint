# Generated by Django 3.1 on 2020-08-16 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200816_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 8, 16, 17, 37, 51, 426537)),
        ),
    ]
