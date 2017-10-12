# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-14 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20170912_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_type_set_for_review', to='contenttypes.ContentType', verbose_name='Content type'),
        ),
    ]
