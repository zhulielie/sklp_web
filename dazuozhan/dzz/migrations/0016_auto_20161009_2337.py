# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzz', '0015_auto_20161009_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xiaofeijilu',
            name='xiaofeishijian',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6d88\u8d39\u65f6\u95f4'),
        ),
    ]
