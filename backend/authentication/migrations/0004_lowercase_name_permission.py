# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-16 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_permission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='Name',
            new_name='name',
        ),
    ]
