# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-27 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20171127_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avaiable',
            field=models.BooleanField(default=True),
        ),
    ]