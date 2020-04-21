from django.contrib import admin

from api.models import Workflow, WorkflowSteps

admin.site.register(Workflow)
admin.site.register(WorkflowSteps)
