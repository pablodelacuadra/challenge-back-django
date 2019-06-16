# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    filter = ('name', 'last_names')
    search_fields = ('name', 'last_names')
    list_display = ('name', 'last_names', 'id')


admin.site.register(User, UserAdmin)
