# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzz', '0010_auto_20161009_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='huiyuan',
            name='last_xiaofeijine',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='\u6700\u8fd1\u4e00\u6b21\u6d88\u8d39\u91d1\u989d'),
        ),
        migrations.AddField(
            model_name='huiyuan',
            name='zongxiaofeicishu',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='\u603b\u6d88\u8d39\u91d1\u989d'),
        ),
        migrations.AddField(
            model_name='huiyuan',
            name='zongxiaofeijine',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='\u603b\u6d88\u8d39\u91d1\u989d'),
        ),
    ]
