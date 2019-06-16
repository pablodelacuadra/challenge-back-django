# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=40)
    last_names = models.CharField(max_length=60)
    django_user = models.OneToOneField(
        "auth.User",
        on_delete=models.CASCADE,
        related_name='django_user')

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __unicode__(self):
        return "{name} {last_names}".format(name=self.name, last_names=self.last_names)