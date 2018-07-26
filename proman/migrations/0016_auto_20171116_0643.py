# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-16 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proman', '0015_auto_20171116_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edu',
            name='college',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='edu',
            name='degree',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='edu',
            name='descrip',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='edu',
            name='endTime',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='edu',
            name='startTime',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='descrip',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='desig',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='endTime',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='firm',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='startTime',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
