# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-01 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20171127_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mode_of_login',
            field=models.CharField(choices=[('S', 'SSO'), ('G', 'Google'), ('L', 'LinkedIn')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
