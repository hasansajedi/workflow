from django.test import TestCase

from .factories import WorkflowFactory
from ..models import Workflow
from ..serializers.serializers import WorkflowSerializer


class WorkflowSerializerTestCase(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Company object for each field."""
        workflow_serializer = WorkflowSerializer()

        self.assertEqual(
            [field for field in workflow_serializer.fields],
            ['name', 'description','steps']
        )
