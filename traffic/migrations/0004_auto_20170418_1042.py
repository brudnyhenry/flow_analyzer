# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0003_auto_20170418_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traffic',
            name='trafficDownload',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='trafficIP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traffic_for_client', to='traffic.Client', unique_for_date='trafficTime'),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='trafficUpload',
            field=models.FloatField(),
        ),
    ]