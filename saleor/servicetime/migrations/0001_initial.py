# Generated by Django 3.2.4 on 2021-06-29 08:05

from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.mixins
import saleor.core.db.fields
import saleor.core.utils.editorjs
import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('dl_delivery_time', models.IntegerField(blank=True, default=0, null=True)),
                ('dl_time_gap', models.IntegerField(blank=True, default=0, null=True)),
                ('dl_as_soon_as_posible', models.BooleanField(blank=True, default=False, null=True)),
                ('dl_allow_preorder', models.BooleanField(blank=True, default=False, null=True)),
                ('dl_preorder_day', models.IntegerField(blank=True, default=0, null=True)),
                ('dl_same_day_order', models.BooleanField(blank=True, default=False, null=True)),
                ('dl_service_time', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
                ('pu_delivery_time', models.IntegerField(blank=True, default=0, null=True)),
                ('pu_time_gap', models.IntegerField(blank=True, default=0, null=True)),
                ('pu_as_soon_as_posible', models.BooleanField(blank=True, default=False, null=True)),
                ('pu_allow_preorder', models.BooleanField(blank=True, default=False, null=True)),
                ('pu_preorder_day', models.IntegerField(blank=True, default=0, null=True)),
                ('pu_same_day_order', models.BooleanField(blank=True, default=False, null=True)),
                ('pu_service_time', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_times', to='store.store')),
            ],
            options={
                'ordering': ('store_id', 'pk'),
                'permissions': (('manage_service_times', 'Service time.'),),
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
        ),
    ]
