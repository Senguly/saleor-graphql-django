# Generated by Django 3.2.4 on 2021-08-11 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_auto_20210722_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='enable_for_big_order',
            field=models.BooleanField(default=False),
        ),
    ]
