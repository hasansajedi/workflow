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

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_at).humanize()

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

    def __unicode__(self) -> str:
        return smart_unicode(self.name)

    def __str__(self) -> str:
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

    def __unicode__(self) -> str:
        return smart_unicode(self.name)

    def __str__(self) -> str:
        return self.name


class Comment(BaseModel):
    id = models.AutoField(primary_key=True)
    workflow_id = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=False, null=False, max_length=350)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ('id',)

    def __unicode__(self) -> str:
        return smart_unicode(self.name)

    def __str__(self) -> str:
        return self.name
