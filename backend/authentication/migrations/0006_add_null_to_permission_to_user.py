# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-16 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_permission_many_to_foreign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='permission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permission_user', to='authentication.Permission'),
        ),
    ]
