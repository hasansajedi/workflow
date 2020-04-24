from factory import DjangoModelFactory, Faker

from ..models import Workflow


class WorkflowFactory(DjangoModelFactory):
    name = Faker('name')
    description = Faker('text')

    class Meta:
        model = Workflow
