# Generated by Django 2.1.5 on 2019-04-12 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookDetails', '0011_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='User',
            field=models.CharField(max_length=50),
        ),
    ]
