# Generated by Django 3.2.4 on 2021-06-29 14:48

from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.mixins
import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('channel', '0001_initial'),
        ('product', '0147_auto_20210623_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(blank=True, max_length=128, null=True)),
                ('required', models.BooleanField(blank=True, default=False, null=True)),
                ('description', models.TextField(blank=True)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='options', to='store.store')),
            ],
            options={
                'ordering': ('name', 'pk'),
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OptionValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option_values', to='product.option')),
            ],
            options={
                'ordering': ('name', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_options', to='product.option')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_options', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='OptionValueChannelListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, null=True)),
                ('channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option_value_channels', to='channel.channel')),
                ('option_value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option_value_channels', to='product.optionvalue')),
            ],
            options={
                'ordering': ('price', 'pk'),
            },
        ),
    ]
