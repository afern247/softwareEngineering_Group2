# Generated by Django 2.1.5 on 2019-04-11 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0009_auto_20190411_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 11, 18, 53, 14, 65517, tzinfo=utc)),
        ),
    ]
