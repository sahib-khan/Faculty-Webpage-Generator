# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-21 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proman', '0021_auto_20171122_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='descrip',
            field=models.CharField(default='+91-361-258XXXX', max_length=200),
        ),
    ]
