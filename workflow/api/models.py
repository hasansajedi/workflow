# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_text as smart_unicode
from shortuuidfield import ShortUUIDField

import arrow
import re


def normalize(query_string):
    """
    Return a tuple of words from a query statement
    Args:
        query_string (TYPE): Description
    Returns:
        TYPE: Description
    """
    terms = re.compile(r'"([^"]+)"|(\S+)').findall(query_string)
    normspace = re.compile(r'\s{2,}').sub
    return (normspace(' ', (t[0] or t[1]).strip()) for t in terms)


class BaseModel(models.Model):
    """
    Abstract model with for all models in our application.

    Attributes:
        created_at (DateTime): Description
        modified_at (DateTime): Description
        uuid (ShortUUID): Description
        archived (Boolean): Description
        deleted (Boolean): Description
    """
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Date Modified"), auto_now=True)
    uuid = ShortUUIDField(null=True, unique=True)
    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        """Summary

        Attributes:
            abstract (bool): Description
        """
        abstract = True

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_at).humanize()

    @classmethod
    def search(cls, query_string):
        """
        Searches the model table for words similar to the query string

        Args:
            query_string (TYPE): Description
        Returns:
            TYPE: Description
        """
        query_terms = normalize(query_string)
        for word in query_terms:
            query_object = models.Q(**{"name__icontains": word})
            return cls.objects.filter(query_object).order_by('date_created')


class Workflow(BaseModel):
    """
    Model the workflow interface

    Parameters
    ----------
        id: integer
            An unique identifier for the workflow
        name: string
            Name for the workflow,
        description: string
            Description for the workflow
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("Name"), blank=False, null=False, max_length=150)
    description = models.TextField(_("Description"), blank=False, null=False, max_length=350)

    class Meta:
        verbose_name = _("Workflow")
        verbose_name_plural = _("Workflows")
        ordering = ('id',)

    def __unicode__(self) -> str:
        """
        Return a human readable representation of the model instance.
        Returns:
            string: The name of workflow
        """
        return smart_unicode("{}".format(self.name))

    def __str__(self) -> str:
        """
        Return a human readable representation of the model instance.
        Returns:
            string: The name of workflow
        """
        return "{}".format(self.name)


class WorkflowSteps(BaseModel):
    """
    Model the workflowstep interface

    Parameters
    ----------
        id: integer,
            An unique identifier for the workflowstep
        workflow_id: integer,
            Refers to an instance of workflow.
        name: string,
            Name for the workflowstep,
        description: string,
            Description for the workflowstep,
        status: char,
            Status of our step.
    """
    DEFINITION = 0
    ACTIVE = 1
    RETIRED = 2

    STATUS_CHOICE_LIST = (
        (DEFINITION, _('In definition')),
        (ACTIVE, _('Active')),
        (RETIRED, _('Retired')),
    )

    id = models.AutoField(primary_key=True)
    workflow_id = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(blank=False, null=False, max_length=150)
    description = models.TextField(blank=False, null=False, max_length=350)
    status = models.IntegerField(_('Status'), choices=STATUS_CHOICE_LIST, default=DEFINITION)

    class Meta:
        verbose_name = _("WorkflowStep")
        verbose_name_plural = _("WorkflowSteps")
        ordering = ('id',)

    def __unicode__(self) -> str:
        """
        Return a human readable representation of the model instance.
        Returns:
            string: The name of workflow
        """
        return smart_unicode(self.name)

    def __str__(self) -> str:
        """
        Return a human readable representation of the model instance.
        Returns:
            string: The name of workflow
        """
        return self.name

    def get_status_display(self, status_code) -> str:
        return self.STATUS_CHOICE_LIST[status_code]


class Comment(BaseModel):
    """
    Model the comment interface

    Parameters
    ----------
        id: integer
            An unique identifier for the comment
        workflow_id: integer
            Refers to an instance of workflow.
        name: string
            Name for the comment,
        text: string
            Description for the comment
    """
    id = models.AutoField(primary_key=True)
    workflow_id = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=False, null=False, max_length=350)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ('id',)

    def __unicode__(self) -> str:
        """
        Return a human readable representation of the model instance.
        Returns:
            string: The name of workflow
        """
        return smart_unicode(self.name)

    def __str__(self) -> str:
        """
        Return a human readable representation of the model instance.
        Returns:
            string: The name of workflow
        """
        return self.name
