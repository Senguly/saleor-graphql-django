# Generated by Django 3.2.4 on 2022-01-07 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_store_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
