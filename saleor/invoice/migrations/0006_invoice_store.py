# Generated by Django 3.2.4 on 2021-06-23 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('invoice', '0005_auto_20210308_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='store.store'),
        ),
    ]
