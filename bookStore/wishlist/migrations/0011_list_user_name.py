# Generated by Django 2.1.5 on 2019-02-23 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0010_remove_list_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='user_name',
            field=models.CharField(default='Testing', max_length=150),
        ),
    ]
