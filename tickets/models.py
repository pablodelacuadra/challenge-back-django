# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

TICKET_STATUS = (
    ('OPEN', 'Abierto'),
    ('PENDING', 'Pendiente'),
    ('IN_PROCESS', 'En Proceso'),
    ('CLOSED', 'Resuelto y cerrado')
)


class Ticket(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=150)
    status = models.CharField(max_length=20, choices=TICKET_STATUS)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ticket"
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __unicode__(self):
        return self.title
