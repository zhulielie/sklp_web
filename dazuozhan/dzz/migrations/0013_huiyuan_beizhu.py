# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzz', '0012_auto_20161009_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='huiyuan',
            name='beizhu',
            field=models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8'),
        ),
    ]
