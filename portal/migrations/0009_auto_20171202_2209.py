# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-02 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20171202_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
