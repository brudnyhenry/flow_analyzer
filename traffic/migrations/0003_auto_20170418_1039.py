# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0002_auto_20170418_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traffic',
            name='trafficDownload',
            field=models.FloatField(unique_for_date='trafficTime'),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='trafficUpload',
            field=models.FloatField(unique_for_date='trafficTime'),
        ),
    ]