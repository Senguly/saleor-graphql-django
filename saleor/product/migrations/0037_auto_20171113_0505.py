# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 11:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0036_auto_20171110_0602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('view_product', 'Can view products'), ('edit_product', 'Can edit products'), ('view_properties', 'Can view product properties'), ('edit_properties', 'Can edit product properties')), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
