# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-30 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzz', '0002_yifu_jiage'),
    ]

    operations = [
        migrations.AddField(
            model_name='yifu',
            name='chengben',
            field=models.CharField(default='', max_length=8, null=True, verbose_name='\u6210\u672c'),
        ),
    ]
