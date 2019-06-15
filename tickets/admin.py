# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from tickets.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    filter = ('title', 'description', 'status')
    list_display = ('id', 'title', 'description', 'status', 'created_at')


admin.site.register(Ticket, TicketAdmin)
