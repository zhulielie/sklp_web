# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzz', '0011_auto_20161009_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='huiyuan',
            name='lianxidizhi',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='\u8054\u7cfb\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='huiyuan',
            name='zongxiaofeicishu',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='\u603b\u6d88\u8d39\u6b21\u6570'),
        ),
    ]
