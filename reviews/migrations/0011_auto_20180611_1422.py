# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-06-11 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20180611_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='source',
            field=models.TextField(blank=True, default='', verbose_name='Source'),
        ),
    ]
