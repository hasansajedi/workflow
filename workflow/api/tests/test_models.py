from django.test import TestCase

from ..models import Workflow, Comment
from .factories import WorkflowFactory


class WorkflowModelTestCase(TestCase):
    """This class defines the test suite for the rasterbucket
    Attributes:
        name (str): Description
        rasterbucket (TYPE): Description
    """

    def setUp(self):
        """Define the test client and other test variables.
        """
        self.name = "Write world class"
        self.description = "Write world class description"
        self.workflow = Workflow(name=self.name, description=self.description)

    def test_model_can_create_a_workflow(self):
        """Test the rasterbucket model can create a rasterbucket.
        """
        old_count = Workflow.objects.count()
        self.workflow.save()
        new_count = Workflow.objects.count()
        self.assertNotEqual(old_count, new_count)


class CompanyTestCase(TestCase):
    def test_str(self):
        """
        Test for string representation.
        """
        workflow_factory = WorkflowFactory()
        self.assertEqual(str(workflow_factory), workflow_factory.name)

    # def test_model_can_create_a_workflow(self):
    #     """
    #     Test the rasterbucket model can create a rasterbucket.
    #     """
    #     workflow_factory = WorkflowFactory()
    #     old_count = Workflow.objects.count()
    #     self.workflow.save()
    #     new_count = Workflow.objects.count()
    #     self.assertNotEqual(old_count, new_count)
