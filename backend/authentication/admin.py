# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import User, Permission


class UserAdmin(admin.ModelAdmin):
    filter = ('name', 'last_names')
    search_fields = ('name', 'last_names')
    list_display = ('name', 'last_names', 'id')


class PermissionAdmin(admin.ModelAdmin):
    filter = ('name',)
    search_fields = ('name',)
    list_display = ('name', 'id')


admin.site.register(User, UserAdmin)
admin.site.register(Permission, PermissionAdmin)
