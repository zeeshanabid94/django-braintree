# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 23:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20171219_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'permissions': (('monthly', 'User is a monthly user'), ('yearly', 'User is an yearly user'), ('database', 'User is a database user'))},
        ),
    ]