# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-08 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dzz', '0004_auto_20160930_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChukuLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='\u64cd\u4f5c\u65f6\u95f4')),
                ('caozuoren', models.CharField(max_length=16, verbose_name='\u6267\u884c\u4eba')),
            ],
            options={
                'verbose_name': '\u51fa\u5e93\u65e5\u5fd7',
                'verbose_name_plural': '\u51fa\u5e93\u65e5\u5fd7',
            },
        ),
        migrations.CreateModel(
            name='RukuLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='\u64cd\u4f5c\u65f6\u95f4')),
                ('caozuoren', models.CharField(max_length=16, verbose_name='\u6267\u884c\u4eba')),
            ],
            options={
                'verbose_name': '\u5165\u5e93\u65e5\u5fd7',
                'verbose_name_plural': '\u5165\u5e93\u65e5\u5fd7',
            },
        ),
        migrations.AlterField(
            model_name='yifu',
            name='dsq',
            field=models.CharField(default='', max_length=8, null=True, verbose_name='\u8bb0\u4e00\u5206'),
        ),
        migrations.AddField(
            model_name='rukulog',
            name='yifu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dzz.Yifu', verbose_name='\u8863\u670d'),
        ),
        migrations.AddField(
            model_name='chukulog',
            name='yifu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dzz.Yifu', verbose_name='\u8863\u670d'),
        ),
    ]