# Generated by Django 3.2.4 on 2022-01-07 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_store_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='description',
            field=models.CharField(blank=True, default=models.CharField(max_length=256), max_length=256, null=True),
        ),
    ]
