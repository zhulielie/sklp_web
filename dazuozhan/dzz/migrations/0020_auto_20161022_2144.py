# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzz', '0019_auto_20161022_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jiagewenjian',
            name='uploadfile',
            field=models.FileField(default='default.png', upload_to='./', verbose_name='\u6210\u672c\u4ef7\u683c\u6587\u4ef6'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='yifu',
            name='uploadfile',
            field=models.FileField(blank=True, default='default.png', null=True, upload_to='./', verbose_name='\u56fe\u7247'),
        ),
    ]