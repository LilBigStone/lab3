# Generated by Django 3.0.5 on 2020-06-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0025_auto_20200621_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='verified_token',
            field=models.CharField(default='HYZKJYMKVX', max_length=10),
        ),
    ]
