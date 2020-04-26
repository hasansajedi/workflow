from django.test import TestCase

from .factories import WorkflowFactory, WorkflowStepFactory
from ..models import Workflow, WorkflowSteps
from ..serializers.serializers import WorkflowSerializer, WorkflowStepSerializer, CommentSerializer, \
    CommentListSerializer, CommentItemSerializer, WorkflowItemSerializer, WorkflowListSerializer


class WorkflowSerializerTestCase(TestCase):
    def test_model_fields(self):
        """
        Serializer data matches the Workflow object for each field.
        """
        workflow_serializer = WorkflowSerializer()

        self.assertEqual(
            [field for field in workflow_serializer.fields],
            ['name', 'description', 'steps']
        )


class WorkflowStepsSerializerTestCase(TestCase):
    def test_model_fields(self):
        """
        Serializer data matches the WorkflowSteps object for each field.
        """
        workflowSteps_serializer = WorkflowStepSerializer()

        self.assertEqual(
            [field for field in workflowSteps_serializer.fields],
            ['id', 'name', 'description', 'status']
        )


class CommentSerializerTestCase(TestCase):
    def test_model_fields(self):
        """
        Serializer data matches the Comment object for each field.
        """
        comment_serializer = CommentSerializer()

        self.assertEqual(
            [field for field in comment_serializer.fields],
            ['workflow_id', 'name', 'text']
        )


class CommentListSerializerTestCase(TestCase):
    def test_model_fields(self):
        """
        Serializer data matches the Comment object for each field.
        """
        commentList_serializer = CommentListSerializer()

        self.assertEqual(
            [field for field in commentList_serializer.fields],
            ['id', 'name', 'text', 'created_at', 'workflow_id']
        )


class CommentItemSerializerTestCase(TestCase):
    def test_model_fields(self):
        """
        Serializer data matches the Comment object for each field.
        """
        commentItem_serializer = CommentItemSerializer()

        self.assertEqual(
            [field for field in commentItem_serializer.fields],
            ['name', 'text', 'created_at']
        )


class WorkflowItemSerializerTestCase(TestCase):
    def test_model_fields(self):
        """
        Serializer data matches the Comment object for each field.
        """
        workflowItem_serializer = WorkflowItemSerializer()

        self.assertEqual(
            [field for field in workflowItem_serializer.fields],
            ['name', 'description', 'steps', 'comments']
        )


class WorkflowListSerializerTestCase(TestCase):
    def test_model_fields(self):
        """
        Serializer data matches the Comment object for each field.
        """
        workflowList_serializer = WorkflowListSerializer()

        self.assertEqual(
            [field for field in workflowList_serializer.fields],
            ['id', 'name', 'description', 'created_at']
        )
