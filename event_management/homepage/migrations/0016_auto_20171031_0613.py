# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-31 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_clubs_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg_user',
            name='Club_id',
            field=models.CharField(default='', max_length=3200),
        ),
        migrations.AddField(
            model_name='reg_user',
            name='Registered_Events',
            field=models.CharField(default='', max_length=3200),
        ),
    ]
