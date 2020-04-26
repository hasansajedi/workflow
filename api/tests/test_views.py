from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Workflow, Comment


class WorkflowViewSetTestCase(TestCase):
    def setUp(self):
        # Initialize client
        self.client = APIClient()

        self.data = {
            "name": "test workflow",
            "description": "description for test workflow",
            "steps": [
                {
                    'name': 'step1',
                    'description': 'description for step1',
                },
                {
                    'name': 'step2',
                    'description': 'description for step2',
                }
            ]
        }
        self.response = self.client.post(
            reverse('api:WorkflowListPost'),
            self.data,
            format="json")

    def test_api_can_post_a_workflow(self):
        """
        Test the api has workflow creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_workflow(self):
        """
        Test the api can get a given workflow.
        """
        workflow = Workflow.objects.get(id=1)
        response = self.client.get(
            reverse('api:WorkflowGetDeleteUpdate',
                    kwargs={'pk': workflow.id}), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, workflow)

    def test_api_can_update_workflow(self):
        """
        Test the api can update a given Workflow.
        """
        workflow = Workflow.objects.get(id=1)
        change_workflow = {"name": "A new workflow",
                           "description": "description for test workflow",
                           "steps": [
                               {
                                   'id': 1,
                                   'name': 'step1',
                                   'description': 'description for step1',
                               },
                               {
                                   'id': 2,
                                   'name': 'step2',
                                   'description': 'description for step2',
                               }
                           ]
                           }
        response = self.client.put(
            reverse('api:WorkflowGetDeleteUpdate', kwargs={'pk': workflow.id}),
            change_workflow, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        """
        Test the api can delete a workflow.
        """
        workflow = Workflow.objects.get(id=1)
        response = self.client.delete(
            reverse('api:WorkflowGetDeleteUpdate', kwargs={'pk': workflow.id}),
            format='json', follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class CommentViewSetTestCase(TestCase):
    def setUp(self):
        # Initialize client to call url
        self.client = APIClient()
        self.workflow = Workflow.objects.create(name="name", description="test description")

        self.data = {
            "workflow_id": self.workflow.id,
            "name": "test comment",
            "text": "comment text goes here"
        }
        self.response = self.client.post(reverse('api:CommentListPost'), self.data, format="json")

    def test_api_can_post_a_comment(self):
        """
        Test the api has comment creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_comment(self):
        """
        Test the api can get a given comment.
        """
        comment = Comment.objects.get(id=1)
        response = self.client.get(reverse('api:CommentGetDeleteUpdate', kwargs={'pk': comment.id}), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, comment)

    def test_api_can_update_a_comment(self):
        """
        Test the api can update a given comment.
        """
        change_comment = {
            "workflow_id": 1,
            "name": "updated comment",
            "text": "updated comment text"
        }
        comment = Comment.objects.get(id=1)
        response = self.client.put(
            reverse('api:CommentGetDeleteUpdate', kwargs={'pk': comment.id}), change_comment, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_delete_a_comment(self):
        """
        Test the api can delete a comment.
        """
        comment = Comment.objects.get(id=1)
        response = self.client.delete(
            reverse('api:CommentGetDeleteUpdate', kwargs={'pk': comment.id}), format='json', follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
