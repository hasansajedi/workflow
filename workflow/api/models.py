from django.db import models
from django.utils.translation import ugettext_lazy as _
from shortuuidfield import ShortUUIDField

import arrow


class Workflow(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=150)
    description = models.TextField(blank=False, null=False, max_length=350)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    uuid = ShortUUIDField(null=True, unique=True)
    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
