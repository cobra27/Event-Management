# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-26 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_reg_user_confirmpass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_user',
            name='ConfirmPass',
            field=models.CharField(default='', max_length=32),
        ),
    ]
