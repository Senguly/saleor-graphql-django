# Generated by Django 3.2.4 on 2022-01-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0167_auto_20220120_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='type',
            field=models.CharField(max_length=128),
        ),
    ]
