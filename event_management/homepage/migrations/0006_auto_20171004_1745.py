# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_reg_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reg_user',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='reg_user',
            old_name='password',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='reg_user',
            old_name='username',
            new_name='Username',
        ),
    ]
