# Generated by Django 3.2.4 on 2021-10-13 06:01

from django.db import migrations, models
import django.db.models.deletion
import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210923_0806'),
        ('order', '0123_alter_order_order_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderevent',
            name='metadata',
            field=models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True),
        ),
        migrations.AddField(
            model_name='orderevent',
            name='private_metadata',
            field=models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True),
        ),
        migrations.AddField(
            model_name='orderevent',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='store.store'),
        ),
    ]
