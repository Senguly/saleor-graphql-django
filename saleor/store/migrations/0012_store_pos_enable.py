# Generated by Django 3.2.4 on 2021-10-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210923_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='pos_enable',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
