# Generated by Django 3.2.4 on 2021-07-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0052_alter_user_language_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
