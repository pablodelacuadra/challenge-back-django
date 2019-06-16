# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-16 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permission',
            field=models.ManyToManyField(related_name='permission_user', to='authentication.Permission'),
        ),
    ]
