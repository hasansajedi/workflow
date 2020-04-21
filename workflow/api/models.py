# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_text as smart_unicode
from shortuuidfield import ShortUUIDField

import arrow


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Date Modified"), auto_now=True)
    uuid = ShortUUIDField(null=True, unique=True)
    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Workflow(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("Name"), blank=False, null=False, max_length=150)
    description = models.TextField(_("Description"), blank=False, null=False, max_length=350)
    uuid = ShortUUIDField(null=True, unique=True)

    class Meta:
        verbose_name = _("Workflow")
        verbose_name_plural = _("Workflows")
        ordering = ('id',)

    def __unicode__(self):
        return smart_unicode(self.name)

    def __str__(self):
        return self.name


class WorkflowSteps(BaseModel):
    id = models.AutoField(primary_key=True)
    workflow_id = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(blank=False, null=False, max_length=150)
    description = models.TextField(blank=False, null=False, max_length=350)

    class Meta:
        verbose_name = _("WorkflowStep")
        verbose_name_plural = _("WorkflowSteps")
        ordering = ('id',)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
