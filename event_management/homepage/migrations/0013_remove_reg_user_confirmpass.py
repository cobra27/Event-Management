# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-26 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20171026_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg_user',
            name='ConfirmPass',
        ),
    ]
