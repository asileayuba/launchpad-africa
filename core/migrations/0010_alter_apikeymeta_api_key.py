# Generated by Django 5.2 on 2025-05-16 03:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_apikeymeta_delete_customapikey'),
        ('rest_framework_api_key', '0005_auto_20220110_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikeymeta',
            name='api_key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta', to='rest_framework_api_key.apikey'),
        ),
    ]
