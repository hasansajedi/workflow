from workflow.wsgi import *
from factory import DjangoModelFactory

from api.models import Workflow, WorkflowSteps


class WorkflowFactory(DjangoModelFactory):
    class Meta:
        model = Workflow

    name = 'workflow name'
    description = 'workflow description'


class WorkflowStepFactory(DjangoModelFactory):
    class Meta:
        model = WorkflowSteps

    workflow_factory = WorkflowFactory()
    workflow_id = workflow_factory
    name = 'name of workflow step'
    description = 'description of workflow step'
    status = 'status of workflow step'
